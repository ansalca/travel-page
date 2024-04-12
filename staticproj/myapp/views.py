from django.shortcuts import render
from .models import Place

# Create your views here.
def home(requset):
    obj = Place.objects.all()
    return render(requset,'index.html',{'result':obj})