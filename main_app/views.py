from django.shortcuts import render

from .models import Catch
# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def catches_index(request):
    catches = Catch.objects.all()
    return render(request, 'catches/index.html', {'catches': catches})

def catches_detail(request, catch_id):
    catch = Catch.objects.get(id=catch_id)
    return render(request, 'catches/detail.html', { 'catch': catch })