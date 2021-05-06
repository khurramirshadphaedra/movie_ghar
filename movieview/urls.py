from django.urls import path
from movieview import views

urlpatterns = [
    path('', views.homepage, name= 'homepage'),
    path('moviedetail', views.movie_details, name="movie_detail"),
    path('movieview', views.movie_view, name="movie_view"),
    path('edit_movie/<int:movieid>', views.edit_movie, name="edit_movie"),
    path('edit_movie/update/<int:movieid>', views.update, name="update"),
    path('delete_movie/<int:movieid>', views.delete_movie, name="delete_movie"),
]
