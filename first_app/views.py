from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world")
def index(request):
    t = "Главная страница"
    return render(request, 'first_app/indedx.html', {'title': t})
