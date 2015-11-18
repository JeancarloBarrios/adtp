from django.shortcuts import render
import os
import glob
import time
from .models import hist
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
# Create your views here.
import RPi.GPIO as GPIO
import time


def home(request):

    return render(request,'p2/home.html',{})


def save(request):
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            # return temp_c, temp_f
            return temp_f

    tmp = read_temp()
    t = float(tmp)
    if t>100.0:
        s = "danger"
    else:
        s = "ok"
    o = hist(temperature=tmp, state=s)

    o.save()
    return render(request, 'p2/home.html', { 'tmp': tmp})


def checktemp(request):

    # os.system('modprobe w1-gpio')
    # os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            # return temp_c, temp_f
            return temp_f

    f = read_temp()
    tmp = f

    return render(request, 'p2/home.html', { 'tmp': tmp})


def show(request):
    db = hist.objects.all()
    return render(request, 'p2/show.html', { 'db': db})

def serve(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    # GPIO.output(3, True)
    if request.method == 'POST':


            print "while"
            p = GPIO.PWM(3, 100)
            p.start(5)
            p.ChangeDutyCycle(4.5)
            time.sleep(0.5)
            # p.ChangeDutyCycle(7.5)
            time.sleep(1)
            # print i
            # print qty
            #i = i + 1
    GPIO.cleanup()


    return render(request, 'medd/home.html', {'medicina': medicina})
