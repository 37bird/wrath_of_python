#use if you know the length, but not the content, of a password. Quicker than the full bruteforce (see wrath_of_python/zip_full_brute.py).

import zipfile
import itertools
import time

# The file name of the zip file, followed by length of the passwords to try. Change as necessary.
zip_file_name = ''
repeat = 4

def extract_file(zippy, paswrd):
    try:
        zippy.extractall(pwd=paswrd)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception, e:
        pass

alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
zip_file = zipfile.ZipFile(zip_file_name)

for c in itertools.product(alphabet, repeat):
    # Slowing it down on purpose to make it work better with web terminals
    # Remove at your peril
    time.sleep(0.001)
    password = ''.join(c)
    print "Trying: %s" % password
    if extract_file(zip_file, password):
        print '*' * 20
        print 'Password found: %s' % password
        print 'Files extracted...'
        exit(0)

# Only occurs if none of the combinations worked
print 'Password not found'
