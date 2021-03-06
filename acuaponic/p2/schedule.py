from django_cron import CronJobBase, Schedule
from . import views
import os
import glob
import time
import logging
from django.http import HttpResponseRedirect, HttpResponse


class updateTemp(CronJobBase):
	RUN_EVERY_MINS = 1 # every minute
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'p2.update_temp' 	# a unique code
	
	def do(self):


		#whatever method to update the temperature and display it


            return HttpResponse("it works")
	
class updateDB(CronJobBase):
	RUN_EVERY_MINS = 60  #Every hour?
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'my_app.update_DB' 	# a unique code
	
	def do(self):
		pass
		#Use whatever sqlite call it is to send the currentTemp to the DB

class trimDB(CronJobBase):
	RUN_AT_TIMES = ['08:00']
	schedule = Schedule(run_at_times=RUN_AT_TIMES)
	code = 'my_app.trim_DB'
	
	def do(self):
		pass
		#Trim down DB so it doesn't get too big on us
