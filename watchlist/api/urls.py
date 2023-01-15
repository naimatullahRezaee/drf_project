from django.urls import path
from watchlist.api import views

urlpatterns = [
    path("stream/<str:pk>/create/", views.Review_View_Create.as_view(), name="create"),
    path("stream/", views.Stream_View_list.as_view(), name="stream-list"),
    path("stream/<str:pk>/", views.Review_View_Detail.as_view(), name="stream-detail"),
    path("review/", views.Review_View_List.as_view(), name="review-list"),
    path("review/<str:pk>/", views.Review_View_Detail.as_view(), name="review-detail"),
    path('list/', views.Watch_View_List.as_view(), name="watch-list"),
    path('<str:pk>/', views.Watch_View_Detail.as_view(), name="watch-detail"),
   
    
]