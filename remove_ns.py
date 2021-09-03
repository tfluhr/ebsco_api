#!/usr/bin/python3

## Removing xml namespaces to make xpath search easier for drupal migrate module

import os
import shutil

my_dir = r'C:\Users\tfluhr\Desktop\pquest_test_2'
ns_rem = ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"'
ns_rem2 = ' xmlns="http://epnet.com/webservices/SearchService/Response/2007/07/"'
ns_rem3 = ' xmlns=""'
replacement = ""

print('hello')

for dirs, subs, files in os.walk(my_dir):
        for fname in files:
                fpath = os.path.join(dirs, fname)
                with open(fpath,  encoding="utf-8") as f:
                        s = f.read()
                s = s.replace(ns_rem, replacement)
                s = s.replace(ns_rem2, replacement)
                s = s.replace(ns_rem3, replacement)
                with open(fpath, "w", encoding="utf-8") as f:
                        f.write(s)
