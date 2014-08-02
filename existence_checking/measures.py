import re 
import hashlib
import os
import time
from existence_hashing.models import Passport
from improved_control.settings import PROJECT_ROOT
from existence_hashing.utils import generate_hash
from existence_checking.main import checking_passports

# Create your tests here.


def test_comparison(f):
    #Setting up
    
    mein_passport = Passport(nationality = "COL", id_passport = "AN343990")

    #Actual Test

    start = time.clock()
    temp = Passport.objects.get(nationality = mein_passport.nationality, id_passport = mein_passport.id_passport)
    print temp.nationality + "<" + temp.id_passport + " HIT"
    end = time.clock()
    total1 = end-start

    f.write("\nGetting from a db: " + str(total1) + "\n")

    start = time.clock()
    if checking_passports(mein_passport.nationality, mein_passport.id_passport, mein_passport.nationality):
        print "HIT!!!!!!!!!"
    end = time.clock()
    total2 = end-start

    f.write("\nChecking in index: " + str(total2) + "\n")

    f.write("\nDifference: " + str(total2 - total1) + "\n")

def measures_main():

    with open(os.path.join(PROJECT_ROOT, 'generated_indexes/Measures_Checking.txt'), 'a') as f:

        print("Welcome to the existence-checking measure set\n")
        f.write("\nMeasures from" + time.strftime("%c") + "\n" )

        print("\nTEST1\n")
        print("This will compare the consult time of the index vs the database")

        choice = input('Do you want to perform this test[y/other]: ')

        if choice == 1:
            f.write("\nTEST1: COMP\n")
            test_comparison(f)
        
        print("\nEOT\n")







