import os
import time
from improved_control.settings import PROJECT_ROOT
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from existence_checking.main import checking_passports
# Create your views here.

key = "XXX"

def index(request):
    context = RequestContext(request, {
        })
    #login
    key = "XXX"
    print key
    return HttpResponse("You're looking at the super awesome checking screen details. These are at the moment unimplemented")

def stats(request):
    return HttpResponse("You're looking at the SLTD-FK-DB details. These are at the moment unimplemented")

def check(request, country, passport):
    #In the future this will get modified with a loop for looking into the possible permissions a country might have
    #import pdb; pdb.set_trace()

    start= time.clock()

    if checking_passports(country, passport, key):
        #print performance
        end= time.clock()
        total = end-start
        print "TOTAL TIME: " + str(total) + "\n"

        return HttpResponse("Passport Exists")
    else:
    	end= time.clock()
        total = end-start
        return HttpResponse("Not found")
