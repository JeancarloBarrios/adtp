from django_cron import CronJobBase, Schedule
from . import views
import os
import glob
import time
import logging
from django.http import HttpResponseRedirect, HttpResponse


class updateTemp(CronJobBase):
	RUN_EVERY_MINS = 5 # every minute
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'p2.update_temp' 	# a unique code

	def do(self):
            print "it worked"


    #whatever method to update the temperature and display it




class updateDB(CronJobBase):
	RUN_EVERY_MINS = 60  #Every hour?
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'p2.update_DB' 	# a unique code

	def do(self):
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
		# Use whatever sqlite call it is to send the currentTemp to the DB

class trimDB(CronJobBase):
	RUN_AT_TIMES = ['08:00']
	schedule = Schedule(run_at_times=RUN_AT_TIMES)
	code = 'my_app.trim_DB'

	def do(self):
		pass
		#Trim down DB so it doesn't get too big on us
