from django.shortcuts import render
from django.http import HttpResponse
from medd.models import Med
from django.shortcuts import get_object_or_404
# Create your views here.
import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, GPIO.OUT)
# Lets define some other stuff'n shit



def display_medicine(request):
    medicina = Med.objects.all()

    return render(request, 'medd/home.html', {'medicina': medicina})

def medicine_search(request, slug):
    search = request.POST.get('slug', 'none')
    test = str(slug)
    if (slug =='none'):
        medicina = Med.objects.all()
    else:
        medicina = Med.objects.get(nombre=test)
        
    return render(request, 'medd/display.html', {'search': search, 'medicina': medicina})
    # return HttpResponse(slug)


def serve(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    # GPIO.output(3, True)
    if request.method == 'POST':
        qty = request.POST.get('qty', None)
        id = request.POST.get('name', None)
        print qty
        i = 0
        c = int(qty)
        for i in range(0, c, 1):

            print "while"
            p = GPIO.PWM(3, 100)
            p.start(5)
            p.ChangeDutyCycle(4.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            print i
            print qty
            #i = i + 1
        GPIO.cleanup()
        print "clean up"
        medicina = Med.objects.all()

    return render(request, 'medd/home.html', {'medicina': medicina})
