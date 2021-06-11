from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import login, logout

# Create your views here.
#def hello(request):
#    return HttpResponse('Hello World')
def index(request):
    id = '001'
    name = 'Attawut'
    email = 'aattawut@gmail.com'
    activities = [
        'Football',
        'Running',
        'Badminton',
    ]

    return render(request, 'index.html',{
        'id': id,
        'name': name,
        'email': email,
        'activities': activities,
    })


def hello(request, id):
    #greeting = 'Your ID: {}'.format(id)
    return HttpResponse('Hello World ID=' + str(id))

# def signin2(request):
#     #greeting = 'Your ID: {}'.format(id)
#     return render(request,'signin.html')


#def article(request):
#   result = 'The article page'
#   return HttpResponse(result)

def article(request, year, slug):
    return HttpResponse('Article Year=' + str(year) + ' Slug=' +slug)



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book:index')
    
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html',{
        'form':form,
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('apptest:index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book:index')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form':form})