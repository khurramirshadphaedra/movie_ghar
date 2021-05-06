from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movies


def homepage(request):
    return render(request, 'homepage.html', {})


def movie_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        shot_desc = request.POST['shot_desc']
        long_desc = request.POST['long_desc']
        thumbnail = request.POST['thumbnail']
        video_url = request.POST['video_url']
        movie = Movies(name=name, shot_desc=shot_desc, long_desc=long_desc,
                       thumbnail=thumbnail, video_url=video_url)
        movie.save()
        messages.success(request, 'Add movie detail  ' + request.POST['name'])
        return redirect(movie_view)
    else:
        return render(request, 'movies/moviedetail.html')


def movie_view(request):
    movie = Movies.objects.all()
    return render(request, 'movies/movieview.html', context={'movie': movie})


def edit_movie(request, movieid):
    movie = Movies.objects.get(id=movieid)
    return render(request, 'movies/editmovie.html', {'movie': movie})


def update(request, movieid):
    movie = Movies.objects.get(id=movieid)
    name = request.POST['name']
    shot_desc = request.POST['shot_desc']
    long_desc = request.POST['long_desc']
    thumbnail = request.POST['thumbnail']
    video_url = request.POST['video_url']
    movie.name = name
    movie.shot_desc = shot_desc
    movie.long_desc = long_desc
    movie.thumbnail = thumbnail
    movie.video_url = video_url
    movie.save()

    return redirect('movie_view')


def delete_movie(request, movieid):
    movie = Movies.objects.get(id=movieid)
    movie.delete()
    return redirect('movie_view')
