
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Catch

from .forms import GearForm
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
    gear_form = GearForm()
    return render(request, 'catches/detail.html', { 
        'catch': catch, 'gear_form': gear_form 
    })

def add_gear(request, catch_id):
    form = GearForm(request.POST)
    if form.is_valid():
        new_gear = form.save(commit=False)
        new_gear.catch_id = catch_id
        new_gear.save()
    return redirect('detail', catch_id=catch_id)

class CatchCreate(CreateView):
    model = Catch
    fields = '__all__'

class CatchUpdate(UpdateView):
    model = Catch
    fields = '__all__'

class CatchDelete(DeleteView):
    model = Catch
    success_url = '/catches/'