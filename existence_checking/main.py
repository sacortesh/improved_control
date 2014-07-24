import os
from existence_hashing.utils import generate_hash
from improved_control.settings import PROJECT_ROOT

def checking_passports(nationality_passport, id_passport, country):
    country_key = find_country_key(country)
    cleartext = nationality_passport + '<' + id_passport
    print cleartext
    ciphertext = generate_hash(cleartext, country_key)
    print ciphertext + country_key


    try:
        exists=check_in_index(ciphertext, country)
        if exists :
            #activate_alerts()
            #log_event()
            print "FOUND!!!!!!!!!!!!!!!!!!!!"
            return True
        else:
            #log_event()
            print "Not found?"
            return False

    except:

        print "IMPOSSIBLE TO ACCESS INDEX"
        #log_event()
        return False

def find_country_key(country):
    #Best security API ever
    return country

def check_in_index(msg, country):
    file_name = os.path.join(PROJECT_ROOT, 'generated_indexes/%s' % country)
    with open(file_name, 'rb') as file_country:
        file_size = os.path.getsize(file_name)
        buffer_size = 4096
        buffer = None
        
        overlap = len(msg) - 1
        while True:
            if (file_country.tell() >= overlap and file_country.tell() < file_size):
                file_country.seek(file_country.tell() - overlap)
            buffer = file_country.read(buffer_size)
            if buffer:
                pos = buffer.find(msg)
                if pos >= 0:
                    return 1
            else:
                return 0
