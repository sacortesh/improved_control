import re 
import hashlib
import os
import time
from django.test import TestCase
from models import Passport, Coop
from utils import generate_index, get_agreements, get_all_passports_by_agreement

# Create your tests here.

class HashingTestCase(TestCase):

    def test_generation_country_st0(self):
        #Setting up
        list_countries = get_agreements("COL")
        print list_countries
        set_passports = get_all_passports_by_agreement(list_countries)


        start = time.clock()
        generate_index(set_passports, "COL", 0)
        end = time.clock()
        total = end-start
        print "generating time took (st0): " + str(total) + "\n"

    def test_generation_country_st1(self):
        #Setting up
        list_countries = get_agreements("XXX")
        print list_countries
        set_passports = get_all_passports_by_agreement(list_countries)

        start = time.clock()
        generate_index(set_passports, "XXX", 1)
        end = time.clock()
        total = end-start
        print "generating time took (st1): " + str(total) + "\n"
