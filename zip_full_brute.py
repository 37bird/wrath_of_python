#If you know the length of the password, please use wrath_of_python/zip_brute_known_length.py. It will save you a lot of time.

import zipfile
import itertools
import time

def extract_file(zippy, paswrd):
    try:
        zippy.extractall(pwd=paswrd)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception, e:
        pass

#path to file
zip_file_name = ""

alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
zip_file = zipfile.ZipFile(zip_file_name)

for i in range(10): #please god let there not be a password longer than 10
    for c in itertools.product(alphabet, repeat=i):
        # Slowing it down on purpose to make it work better with web terminals
        # Remove at your peril
        time.sleep(0.001)
        ''.join(c)
        print "Trying: %s" % password
        if extract_file(zip_file, password):
            print '*' * 20
            print 'Password found: %s' % password
             print 'Files extracted...'
             exit(0)

# If no password was found by the end, tell us
print 'Password not found, try adding special characters to the alphabet.'
