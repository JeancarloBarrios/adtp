from django.shortcuts import render
from . import models
# Create your views here.

def display_medicine(request):
    medicina = med.objects.all()

    return render(request, '', {'medicina': medicina})

def medicine_search(request):
    search = request.POST['search']

    if (search ==""):
        medicina = med.objects.all()
    else:
        medcine = med.objects.filter(nombre=search)
    return render(request, '', {'search': search, 'medicina': medicina})
