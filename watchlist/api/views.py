from watchlist.models import Watch, Review, StreamPlatform
from watchlist.api.serializers import WatchSerializer, ReviewSerializer, StreamSerializer
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError



class Review_View_Create(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watch.objects.get(pk=pk)
    
        review_user = self.request.user
        review_queryset = Review.objects.filter(watch=watchlist, writer=review_user)

        if review_queryset.exists():
            raise ValidationError("you have already reviewed this movie")

        serializer.save(watch=watchlist, writer=review_user)
   

class Review_View_List(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        review = Review.objects.all()
        return review


class Review_View_Detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self ,request, *args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self , request, *args, **kwargs):
        return self.update(request,*args, **kwargs)
        
    def delete(self , request, *args, **kwargs):
        return self.destroy(request,*args , **kwargs)   



class Watch_View_List(generics.ListCreateAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer

    


class Watch_View_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer


class Stream_View_list(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSerializer

class Stream_View_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSerializer




# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serialiser = MovieSerializer(movies, many=True)
#         return Response(serialiser.data)

#     if request.method == "POST":
#         serialiser = MovieSerializer(data=request.data)
#         if serialiser.is_valid():
#             serialiser.save()
#             return Response(serialiser.data)
#         else:
#             return Response(serialiser.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         movies = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movies = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response()

