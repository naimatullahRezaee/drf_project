# from django.shortcuts import render
# from watchlist.models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'Movie': list(movies.values())
#     }

#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movies = Movie.objects.get(pk=pk)
#     data = {
#         'name': movies.name,
#         'description': movies.description,
#         'active': movies.active
#     }

#     return JsonResponse(data)