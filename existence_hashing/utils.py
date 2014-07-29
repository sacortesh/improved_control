import re 
import hashlib
import os
import time
from Queue import Queue
from threading import Thread, activeCount
from improved_control.settings import PROJECT_ROOT
from models import Passport, Coop

num_worker_threads = 4
hashing_queue = Queue()
writing_queue = Queue()

def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def generate_hash(msg, salt):
    m = hashlib.md5()
    m.update(salt + msg)
    m2 = hashlib.md5()
    m2.update(msg + m.hexdigest() + msg)
    print "h"
    return m2.hexdigest()

def generate_index(set_passports, country):
    start= time.clock()
    #	import pdb; pdb.set_trace()
    flag = True
    try:

        file_country = open(os.path.join(PROJECT_ROOT, 'generated_indexes/%s' % country), "w")

        for i in range(num_worker_threads-1):
            t = Thread(target=hashing_daemon, args=(country,))
            t.daemon = True
            t.start()

	
        t = Thread(target=write_to_disk_daemon, args=(file_country,))
        t.daemon = True
        t.start()
	        

        #TODO generate a true salt per country
        for passport in set_passports:
            hashing_queue.put(passport.nationality + '<' + passport.id_passport)

        #enclosure_queue.put("STOP")
        hashing_queue.join()	
        writing_queue.join()	
        
	file_country.close()
        end= time.clock()
        total = end-start
        print "generating time took: " + str(total) + "\n"
    except:
        flag = False
    return flag

def get_agreements(country):
    """ Gets the list of countries that the country argument has an agreement with. """
    start= time.clock()
    list_countries = set()
    list_countries.add(unicode(country))

    list_agreements = Coop.objects.raw("SELECT `COOP`.`id_agreement`, `COOP`.`country_a`, `COOP`.`country_b` FROM `COOP` WHERE `COOP`.`country_a` = %s OR `COOP`.`country_b` = %s ", [country , country])
    for each in list_agreements:
        list_countries.add(each.country_a)
        list_countries.add(each.country_b)


    end= time.clock()
    total = end-start
    print "obtaining agreements took: " + str(total) + "\n"

    return list_countries

def countries_to_sql(list_countries):
    """ Transforms a set of countries into an actual SQL statement, crafted specifically for looking into the passport database. """
    start= time.clock()
    starting_string = "SELECT * FROM `PASSPORT` WHERE "
    countries_string = ""
    for each_element in list_countries:
        if countries_string == "":
            countries_string+="`PASSPORT`.`nationality` LIKE '" + each_element + "' "
        else:
            countries_string+="OR `PASSPORT`.`nationality` LIKE '" + each_element + "' "
    end= time.clock()
    total = end-start
    print "generating raw sql request: " + str(total) + "\n"
    starting_string+=countries_string
    return starting_string

def get_all_passports_by_agreement(list_countries):
    raw_sql_statement = countries_to_sql(list_countries)
    set_passports = set()
    start= time.clock()

    queryset_passports=Passport.objects.raw(raw_sql_statement)

    #for each_queryset in queryset_passports:
    #   	set_passports.add(each_queryset)
    #    print each_queryset


    end= time.clock()
    total = end-start
    print "generating treatable list: " + str(total) + "\n"
    return queryset_passports

def write_to_disk_daemon(outfile):
    while True:
        msg = writing_queue.get()
        outfile.write(msg + "\n")
        print "."
        writing_queue.task_done()

def hashing_daemon(country):
    while True:
        msg = hashing_queue.get()
        writing_queue.put(generate_hash(msg,country))
        print "_"     
        hashing_queue.task_done()


def look_for_collisions(country):
    with open(os.path.join(PROJECT_ROOT, 'generated_indexes/%s' % country)) as f:
        seen = set()
        for line in f:
            line_lower = line.lower()
            if line_lower in seen:
                print(line)
            else:
                seen.add(line_lower)

def create_all_files(strategy=0):
    if strategy == 0:
        set_countries_agreements = set()
        file_countries = open(os.path.join(PROJECT_ROOT, 'list_countries'))
        set_countries_temp = set(line.strip() for line in file_countries)
        file_countries.close()
        set_countries = sorted_nicely(set_countries_temp)

        for each_country in set_countries:
            set_agreements = frozenset(get_agreements(each_country))
            set_countries_agreements.add(set_agreements)

        print("All agreements obtained")

        set_passports = Passport.objects.all()

        print("All passports obtained")


        for each_passport in set_passports:
            for each_agreement in set_countries_agreements:
                for each_country in each_agreement:
                    if each_passport.nationality == each_country:
                        with open(os.path.join(PROJECT_ROOT, 'generated_indexes/%s' % iter(each_agreement).next()), "a") as f:
                            f.write(generate_hash(each_passport.nationality + "<" + each_passport.id_passport, each_country) + "\n")
                    print(".")
                print("_")
            print("-")
        print("~")






