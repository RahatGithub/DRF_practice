from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookAPI(APIView):
    
    # serves FETCH ALL BOOKS and FETCH BOOK
    def get(self, request, id=None):
        if id:
            try:
                book = Book.objects.get(id=id)
                # get all author names
                author_names = [author.name for author in book.authors.all()]
                # construct the JSON response
                response_data = {
                    'id': book.id,
                    'title': book.title,
                    'genre': book.genre,
                    'price': book.price,
                    'publication': book.publication.name,  # Assuming publication is a ForeignKey
                    'authors': author_names
                }
                return Response(response_data, status=200)
            except Book.DoesNotExist:
                return Response({"message": f"book with id: {id} was not found"}, status=404)  
        else:
            books = get_the_books(request) 
            return Response({"books" : books}, status=200)
    
    
    # serves ADD BOOKS
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"message" : "invalid request!"})


    # serves UPDATE BOOKS
    def put(self, request, id):
        return update_book(request, id)
    

    # serves UPDATE BOOKS PARTIALLY
    def patch(self, request, id):
        return update_book(request, id)


    # serves DELETE BOOKS
    def delete(self, request, id):
        try: 
            book = Book.objects.get(id=id)
            book.delete() 
        except:
            return Response({"message" : f"book with id: {id} was not found"})
        return Response({"message" : f"deleted book with id: {id}"})



# *************SUPPORTIVE FUNCTIONS*************

# generates a dull dictionary of the object to return because bodies of PUT and PATCH requests don't contain the full object
def generate_full_dict(id, serializer_data):
        result_dict = dict({'id' : int(id)})
        additional_dict = dict(serializer_data)
        result_dict.update(additional_dict)
        return result_dict


# called from PUT and PATCH to update book fully or partially
def update_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response({"message": f"book with id: {id} was not found"}, status=404)

    partial = True # by default we're assuming it's a PATCH request
    if request.method == 'PUT': 
        partial = False
    
    serializer =  BookSerializer(book, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        result = generate_full_dict(id, serializer.data)
        return Response(result, status=200)
    return Response(serializer.error, status=400)



# checks if anything is being searched or not and returns the books accordingly
def get_the_books(request):

    # fetching all books
    queryset = Book.objects.all()

    # checking the query parameters which may or may not exist
    title = request.GET.get('title')
    author = request.GET.get('author')
    genre = request.GET.get('genre')
    sort_field = request.GET.get('sort', 'id') # by default sort_field = 'id' 
    order = request.GET.get('order', 'ASC')  # by default order = 'ASC' 

    if title:
        queryset = queryset.filter(title=title)
    elif author:
        queryset = Book.objects.filter(authors__name=author)
    elif genre:
        queryset = queryset.filter(genre=genre)                    

    if order == 'DESC': # by default 'ASC'
        sort_field = '-' + sort_field
    
    # sorting the queryset
    queryset = queryset.order_by(sort_field)

    serializer = BookSerializer(queryset, many=True)
    return serializer.data