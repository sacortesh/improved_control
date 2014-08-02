import re 
import hashlib
import os
import time
from models import Passport, Coop
from improved_control.settings import PROJECT_ROOT
from utils import generate_index, get_agreements, get_all_passports_by_agreement, look_for_collisions, create_all_files

# Create your tests here.


def test_generation_country_st0(f):
    #Setting up
    list_countries = get_agreements("COL")
    set_passports = get_all_passports_by_agreement(list_countries)


    start = time.clock()
    generate_index(set_passports, "COL", 0)
    end = time.clock()
    total = end-start
    f.write("generating time took (st0): " + str(total) + "\n")

def test_generation_country_st1(f):
    #Setting up
    list_countries = get_agreements("ARG")
    set_passports = get_all_passports_by_agreement(list_countries)

    start = time.clock()
    generate_index(set_passports, "ARG", 1)
    end = time.clock()
    total = end-start
    f.write("generating time took (st1): " + str(total) + "\n")

def test_collisions(f):
    f.write(look_for_collisions("COL"))


def test_full_generation(f, st):
    start = time.clock()
    create_all_files(st)
    end = time.clock()
    total = end-start
    f.write("generating time took for (" + str(st) +"): " + str(total) + "\n")

def measures_main():

    with open(os.path.join(PROJECT_ROOT, 'generated_indexes/Measures.txt'), 'a') as f:

        print("Welcome to the existence-hashing measure set\n")
        f.write("\nMeasures from" + time.strftime("%c") + "\n" )

        print("\nTEST1\n")
        print("This will generate the index of existence for COL using threaded strategy")

        choice = input('Do you want to perform this test[y/other]: ')

        if choice == 'Y':
            f.write("\nTEST1: COLTHREADED\n")
            test_generation_country_st0(f)
            f.write("\nAssociated file size: " + str(os.path.getsize(os.path.join(PROJECT_ROOT, 'generated_indexes/COL'))))

        print("\nTEST2\n")
        print("This will generate the index of existence for ARG using pythons default strategy")

        choice = input('Do you want to perform this test[y/other]: ')

        if choice == 1:
            f.write("\nTEST2: ARGNORMAL\n")
            test_generation_country_st1(f)
            f.write("\nAssociated file size: " + str(os.path.getsize(os.path.join(PROJECT_ROOT, 'generated_indexes/ARG'))))

        print("\nTEST3\n")
        print("This will verify in the index of COL if a collision was produced")

        choice = input('Do you want to perform this test[y/other]: ')

        if choice == 1:
            f.write("\nTEST3: COLCOLLISION\n")
            test_collisions(f)


        print("\nTEST4\n")
        print("This will measure the time it would take to generate all the files. Requires a strong machine or the process will break")

        choice = input('Do you want to perform this test[y/other] (it will take a while): ')

        if choice == 1:
            f.write("\nTEST4: ALL1\n")
            test_full_generation(f,0)

        print("\nTEST5\n")
        print("This will measure the time it would take to generate all the files (second strategy)")

        choice = input('Do you want to perform this test[y/other] (it will take a while): ')

        if choice == 1:
            f.write("\nTEST4: ALL2\n")
            test_full_generation(f,1)







