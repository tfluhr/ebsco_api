import requests
import math
import lxml.etree as ET


ebsco_profile = "s5681754.main.eit"
ebsco_pass = "CHANGEMEXXXX"
query_string = "hierarchy"

query_strings = [
    "hierarchy",
    "hierarchies",
    "hierarchical",
    "hierarchic",
    "hierarchism"
    ]

search_fields = [
    "TI", # title
    "SU", # Subject
    "AB", # Absract
    "KW" # Keywords
]

journals = [
    "00029602", # American Journal of Sociology
    "00031224", # American Sociological Review
    "00377732" # Social Forces
]

uids = []

for qs in query_strings:
    for sf in search_fields:
        for j in journals:
            call = str("https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof={}&pwd={}&query={}+{}+AND+IS+{}&db=sih&numrec=200".format(ebsco_profile, ebsco_pass, sf, qs, j))
            #print(call)
            r = requests.get(call)
            tree = ET.ElementTree(ET.fromstring(r.content))
            root = tree.getroot()
            hits = root.find('{http://epnet.com/webservices/SearchService/Response/2007/07/}Hits').text
            print(hits, call)
            # This commented section would be needed if any query returned more than 200 results
            #offset = 201
            ## only the first 200...need to grab the next x and add to list
            for rec in root.iter('header'):
                uid = rec.attrib['uiTerm']
                if uid not in uids:
                    uids.append(uid)

print(len(uids))
