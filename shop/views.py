from django.shortcuts import render
from .models import Coffee
# Create your views here.
def home(request):
    coffees = Coffee.objects.all()
    return render(request, 'home.html', {'coffees': coffees})