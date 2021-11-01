from django.shortcuts import render
from .models import MyBetModel

# Create your views here.


def index(request):
    objects = MyBetModel.objects.all()
    return render(request, 'profeta/index.html', {"objects": objects})