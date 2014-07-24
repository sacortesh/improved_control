import os
import time
from improved_control.settings import PROJECT_ROOT
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from existence_hashing.utils import sorted_nicely, generate_index, get_agreements, get_all_passports_by_agreement
from existence_hashing.models import Passport
# Create your views here.

def index(request):
    file_countries = open(os.path.join(PROJECT_ROOT, 'list_countries'))
    set_countries_temp = set(line.strip() for line in file_countries)
    file_countries.close()
    set_countries = sorted_nicely(set_countries_temp)
    template= loader.get_template('existence_hashing/index.html')
    context = RequestContext(request, {
        'set_countries': set_countries,
    })
    return HttpResponse(template.render(context))

def stats(request):
    return HttpResponse("You're looking at the SLTD-FK-DB details. These are at the moment unimplemented")

def generate(request, country):
    #In the future this will get modified with a loop for looking into the possible permissions a country might have
    #import pdb; pdb.set_trace()

    start= time.clock()

    list_countries = get_agreements(country)
    set_passports = get_all_passports_by_agreement(list_countries)
    
    if generate_index(set_passports, country):
        #print performance
        end= time.clock()
        total = end-start
        print "TOTAL TIME: " + str(total) + "\n"

        return HttpResponse("Database generated for %s" %country)
    else:
        return HttpResponse("Imposible to generate the index for %s" %country)
