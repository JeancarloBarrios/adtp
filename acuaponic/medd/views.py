from django.shortcuts import render
from medd.models import Med
# Create your views here.

def display_medicine(request):
    medicina = Med.objects.all()

    return render(request, 'medd/home.html', {'medicina': medicina})

def medicine_search(request):
    search = request.POST['search']

    if (search ==""):
        medicina = Med.objects.all()
    else:
        medcine = Med.objects.filter(nombre=search)
    return render(request, '', {'search': search, 'medicina': medicina})
