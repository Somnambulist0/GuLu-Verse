from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import UserProfile


# Create your views here.

def index0(request):
    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        return render(request, 'user_index0.html', {'profile': profile})
    else:
        return render(request, 'index0.html')

def main(request):
    return render(request, 'main.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['loginUsername']
        password = request.POST['loginPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index0')  # Redirect to your desired page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['registerUsername']
        password = request.POST['registerPassword']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    return render(request, 'register.html')

def about_view(request):
    return render(request, 'about.html')

def todo_view(request):
    return render(request, 'todo.html')

# def recommend_view(request):
#     return render(request, 'recommend.html')

from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Movie
from .services import movie_recommendation_logic
import json


@csrf_exempt 
def recommend_movies_view(request):
    if request.method == 'POST':
    #Json date from the front end(response)
        data = json.loads(request.body)
        mood = data.get('mood')
        classic = data.get('classic')
        noisy = data.get('noisy')
        reality = data.get('reality')
        alone = data.get('alone')

        movies = Movie.objects.all()

        # logic
        recommended_movies = movie_recommendation_logic(mood, classic, noisy, reality, alone, movies)
        recommended_movies_dicts = [movie.to_dict() for movie in recommended_movies]

        request.session['recommended_movies'] = recommended_movies_dicts
        
        return HttpResponseRedirect('/display_recommendations/')
    
    else:
        return HttpResponseNotAllowed(['POST'])
    
# def display_recommendations_view(request):
#     recommended_movies_dicts = request.session.get('recommended_movies', [])
#     return render(request, 'recommend_movies.html', {'movies': recommended_movies_dicts})

def display_recommendations_view(request):
    recommended_movies = request.session.get('recommended_movies', [])
    context = {
        'movie1': recommended_movies[0] if len(recommended_movies) > 0 else None,
        'movie2': recommended_movies[1] if len(recommended_movies) > 1 else None,
        'movie3': recommended_movies[2] if len(recommended_movies) > 2 else None,
        'movie1_type': recommended_movies[0].get('classification', {}).get('type') if len(recommended_movies) > 0 else None,
        'movie2_type': recommended_movies[1].get('classification', {}).get('type') if len(recommended_movies) > 1 else None,
        'movie3_type': recommended_movies[2].get('classification', {}).get('type') if len(recommended_movies) > 2 else None,
    }
    return render(request, 'recommend_movies.html', context)


#sent email
@csrf_exempt
@require_http_methods(["POST"])
def submit_form(request):
    data = json.loads(request.body)
    name = data.get('name')
    email = data.get('email')

    # send email to admin
    send_mail(
        'New Join Us Submission',
        f'Name: {name}\nEmail: {email}',
        'serviceguluverse@outlook.com',  
        ['serviceguluverse@outlook.com'],  
        fail_silently=False,
    )

    # send email to user
    send_mail(
        'Thank you for your submission',
        f'Hi {name}:\nThank you for your submission to join us!',
        'serviceguluverse@outlook.com',  
        [email],
        fail_silently=False,
    )

    return JsonResponse({'message': 'Form submitted successfully'})







