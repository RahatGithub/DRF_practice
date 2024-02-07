from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Publication
from .serializers import PublicationSerializer


class PublicationAPI(APIView):
    
    # serves FETCH ALL BOOKS and FETCH BOOK
    def get(self, request, id=None):
        if id:
            try:
                publication = Publication.objects.get(id=id)
                serializer = PublicationSerializer(publication)
                return Response(serializer.data, status=200)
            except Publication.DoesNotExist:
                return Response({"message": f"publication with id: {id} was not found"}, status=404)  
        else:
            publications = get_the_publications(request) 
            return Response({"publications" : publications}, status=200)
    
    
    # serves ADD BOOKS
    def post(self, request):
        data = request.data
        serializer = PublicationSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"message" : "invalid request!"})


    # serves UPDATE BOOKS
    def put(self, request, id):
        return update_publication(request, id)
    

    # serves UPDATE BOOKS PARTIALLY
    def patch(self, request, id):
        return update_publication(request, id)


    # serves DELETE BOOKS
    def delete(self, request, id):
        try: 
            publication = Publication.objects.get(id=id)
            publication.delete() 
        except:
            return Response({"message" : f"publication with id: {id} was not found"})
        return Response({"message" : f"deleted publication with id: {id}"})



# *************SUPPORTIVE FUNCTIONS*************

# generates a dull dictionary of the object to return because bodies of PUT and PATCH requests don't contain the full object
def generate_full_dict(id, serializer_data):
        result_dict = dict({'id' : int(id)})
        additional_dict = dict(serializer_data)
        result_dict.update(additional_dict)
        return result_dict


# called from PUT and PATCH to update publication fully or partially
def update_publication(request, id):
    try:
        publication = Publication.objects.get(id=id)
    except Publication.DoesNotExist:
        return Response({"message": f"publication with id: {id} was not found"}, status=404)

    partial = True # by default we're assuming it's a PATCH request
    if request.method == 'PUT': 
        partial = False
    
    serializer =  PublicationSerializer(publication, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        result = generate_full_dict(id, serializer.data)
        return Response(result, status=200)
    return Response(serializer.error, status=400)



# checks if anything is being searched or not and returns the publications accordingly
def get_the_publications(request):

    # fetching all publications
    queryset = Publication.objects.all()

    # checking the query parameters which may or may not exist
    name = request.GET.get('name')
    starting_year = request.GET.get('starting_year')
    sort_field = request.GET.get('sort', 'id') # by default sort_field = 'id' 
    order = request.GET.get('order', 'ASC')  # by default order = 'ASC' 

    if name:
        queryset = queryset.filter(name=name)
    elif starting_year:
        queryset = queryset.filter(starting_year=starting_year)
    if order == 'DESC': # by default 'ASC'
        sort_field = '-' + sort_field
    
    # sorting the queryset
    queryset = queryset.order_by(sort_field)

    serializer = PublicationSerializer(queryset, many=True)
    return serializer.data