from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_list_or_404, redirect
from .models import Movie

# Create your views here.

from django.http import HttpResponse
# Create your views here.

def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})
    
from django.shortcuts import render, get_object_or_404
from .models import Movie

from django.shortcuts import render, get_object_or_404
from .models import Movie

def update(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        for field in ['title', 'director', 'release_date', 'genre', 'duration']:
            setattr(movie, field, request.POST[field])
        movie.save()
        return render(request, 'movies/update.html', {'movie': movie, 'success': True})

    return render(request, 'movies/update.html', {'movie': movie})
    
def delete(request, movie_id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
    return redirect('movies:index')

# Create your views here.
