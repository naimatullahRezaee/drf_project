from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serialiser = MovieSerializer(movies, many=True)
        return Response(serialiser.data)

    if request.method == "POST":
        serialiser = MovieSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        else:
            return Response(serialiser.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)

    if request.method == 'PUT':
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        movies = Movie.objects.get(pk=pk)
        movies.delete()
        return Response()

