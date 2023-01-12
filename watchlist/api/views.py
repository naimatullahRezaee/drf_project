from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serialiser = MovieSerializer(movies, many=True)

    return Response(serialiser.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)


    