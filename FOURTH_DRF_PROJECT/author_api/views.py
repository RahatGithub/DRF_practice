from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author 
from .serializers import AuthorSerializer


class AuthorAPI(APIView):
    
    # serves FETCH ALL authorS and FETCH author
    def get(self, request, id=None):
        if id:
            try:
                author = Author.objects.get(id=id)
                serializer = AuthorSerializer(author)
                return Response(serializer.data, status=200)
            except Author.DoesNotExist:
                return Response({"message": f"author with id: {id} was not found"}, status=404)  
        else:
            authors = get_the_authors(request) 
            return Response({"authors" : authors}, status=200)
    
    
    # serves ADD authorS
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"message" : "invalid request!"})


    # serves UPDATE authorS
    def put(self, request, id):
        return update_author(request, id)
    

    # serves UPDATE authorS PARTIALLY
    def patch(self, request, id):
        return update_author(request, id)


    # serves DELETE authorS
    def delete(self, request, id):
        try: 
            author = Author.objects.get(id=id)
            author.delete() 
        except:
            return Response({"message" : f"author with id: {id} was not found"})
        return Response({"message" : f"deleted author with id: {id}"})



# *************SUPPORTIVE FUNCTIONS*************

# generates a dull dictionary of the object to return because bodies of PUT and PATCH requests don't contain the full object
def generate_full_dict(id, serializer_data):
        result_dict = dict({'id' : int(id)})
        additional_dict = dict(serializer_data)
        result_dict.update(additional_dict)
        return result_dict


# called from PUT and PATCH to update author fully or partially
def update_author(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response({"message": f"author with id: {id} was not found"}, status=404)

    partial = True # by default we're assuming it's a PATCH request
    if request.method == 'PUT': 
        partial = False
    
    serializer =  AuthorSerializer(author, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        result = generate_full_dict(id, serializer.data)
        return Response(result, status=200)
    return Response(serializer.error, status=400)



# checks if anything is being searched or not and returns the authors accordingly
def get_the_authors(request):

    # fetching all authors
    queryset = Author.objects.all()

    # checking the query parameters which may or may not exist
    name = request.GET.get('name')
    gender = request.GET.get('gender')
    sort_field = request.GET.get('sort', 'id') # by default sort_field = 'id' 
    order = request.GET.get('order', 'ASC')  # by default order = 'ASC' 
    
    if name:
        queryset = queryset.filter(name=name)
    elif gender:
        queryset = queryset.filter(gender=gender)
    if order == 'DESC': # by default 'ASC'
        sort_field = '-' + sort_field
        
    # sorting the queryset
    queryset = queryset.order_by(sort_field)

    serializer = AuthorSerializer(queryset, many=True)
    return serializer.data