from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login, logout

from account.models import Score

from .forms import CustomUserForm, ScoreForm
from .email_backend import EmailBackend
from django.contrib import messages


# Create your views here.
def registration(request):
    form = CustomUserForm(request.POST or None, request.FILES or None)
    context = {
        'form' : form,
        'title' : 'Mentor - Registration',
        'sub_title' : 'Registration',
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('login-page'))
    return render(request, 'account/register.html', context)

def loginpage(request):
    context = {
        'title' : 'Mentor - Login',
        'sub_title' : 'Login',

    }
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'ACCESS GRANTED!!')
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'INVALID EMAIL/PASSWORD')
            return redirect(reverse('login-page'))
            
    return render(request, 'account/login.html', context)

def dashboard(request):
    scores = Score.objects.all()
    context= {
         'title' : 'Mentor - Dashboard',
        'sub_title' : 'Dashboard',
        'saved_scores' : scores
    }
    return render(request, 'account/dashboard.html', context)

def logoutpage(request):
    try:
        logout(request)
        messages.success(request, 'LOGGED OUT')
        return redirect(reverse('login-page'))
    except:
        pass
    return redirect(reverse('login-page'))

def add_scores(request):
    scores = ScoreForm(request.POST or None)
    context = {
        'scores' : scores,
        'title' : 'Mentor - Add Scores',
        'sub_title' : 'Add Scores',
        
    }
    if request.POST:
        if scores.is_valid():
            scores.save()
            return redirect(reverse('dashboard'))
    return render(request, 'account/add_score.html', context)