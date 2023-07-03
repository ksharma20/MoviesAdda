from django.shortcuts import redirect, render
from Dashboard.models import FavMovies

from Home.models import Movies

# Create your views here.
def dash(request):
    if request.user.is_authenticated:
        context = {'Movies': reversed(Movies.objects.all())}
        context['FavMovies'] = FavMovies.objects.filter(user=request.user)
        return render(request, 'dashboard.html', context)


    return redirect('/')

def add(request, id):
    if request.user.is_authenticated:
        movie = Movies.objects.get(id=id)
        FavMovies.objects.get_or_create(name=movie, user=request.user)
        return redirect('/dashboard/')
    
    return redirect('/')

def remove(request, id):
    if request.user.is_authenticated:
        FavMovies.objects.get(id=id).delete()
        return redirect('/dashboard/')
    
    return redirect('/')
