from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Home.models import Movies
from Dashboard.models import FavMovies

# Create your views here.
def home(request):
    # console.log($.getJSON("https://api.themoviedb.org/3/discover/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb"));
    if request.method == 'POST':
        mn = request.POST.get('mn')
        Movies.objects.create(name=mn)

    context = {}
    movies = Movies.objects.all()

    mr = [0,0,0]
    mn = ['', '', '']
    for movie in movies:
        fav = len(FavMovies.objects.filter(name = movie.id))
        movie.rate = int((fav/len(User.objects.all()))*100)
        if movie.rate > mr[0]:
            mr[2] = mr[1]
            mn[2] = mn[1]
            mr[1] = mr[0]
            mn[1] = mn[0]
            mr[0] = movie.rate
            mn[0] = movie.name
        elif movie.rate > mr[1]:
            mr[2] = mr[1]
            mn[2] = mn[1]
            mr[1] = movie.rate
            mn[1] = movie.name
        elif movie.rate > mr[2]:
            mr[2] = movie.rate
            mn[2] = movie.name

        movie.save()

    context['Movies'] = reversed(movies)
    context['featured'] = {'1': mn[0], '2': mn[1], '3': mn[2]}
    
    if request.user.is_authenticated:
        context['user_logged'] = True
    
    return render(request, 'home.html', context)

def ulogin(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = authenticate(request, username=uname, password=passwd)
        if user:
            login(request, user)
            return redirect('/dashboard/')
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('/')
        

def uregister(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        cpasswd = request.POST.get('cpasswd')
        if passwd == cpasswd:
            user, created = User.objects.get_or_create(username=uname)
            if created:
                user.set_password(passwd)
                user.name = name
                user.email = email
                user.save()
                return redirect('/')
            else:
                context['message'] = 'Username Already Exists'
        else:
            context['message'] = 'Wrong Password'

    return render(request, 'register.html', context)