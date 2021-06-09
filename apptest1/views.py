from django.shortcuts import render
from django.http import HttpResponse

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


#def article(request):
#   result = 'The article page'
#   return HttpResponse(result)

def article(request, year, slug):
    return HttpResponse('Article Year=' + str(year) + ' Slug=' +slug)

