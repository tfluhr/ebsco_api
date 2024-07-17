import requests
import math
import lxml.etree as ET
import csv

##################
## Define stuff
##################

log_path = (r'C:\\Temp\query_log.txt')
csv_path = (r'C:\\Temp\ebsco.csv')

ns = "{http://epnet.com/webservices/SearchService/Response/2007/07/}"
ebsco_profile = "XxXXXXXX"
ebsco_pass = "XXXXXX"

# terms to search form
query_strings = [
    "hierarchy",
    "hierarchies",
    "hierarchical",
    "hierarchic",
    "hierarchism"
    ]

# fields to search for query strings
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
#my_uids_filtered = []

# metadata fields to search
md_fields = {
    "j_title": ".//jinfo/jtl",
    "pub_date": ".//pubinfo/dt",
    "doi": ".//ui[@type=\"doi\"]",
    "a_title": ".//tig/atl",
    #"authors": ".//aug/au"
    "abstract": ".//artinfo/ab"
}

## metadata fields to search with multiple values.  Need to handle differently
mv_md_fields = {
    "authors": ".//aug/au",
    "subjects": ".//artinfo/su",
    "keywords": ".//artinfo/keyword"
}

# Create list of headers for csv datafile
headers = []

##########################
## Get UIDS of articles that contain search terms
##########################

for query in query_strings:
    for sf in search_fields:
        for journal in journals:
            call = ("https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof={}&pwd={}&query={}+{}+AND+ISSN+{}&db=sih&numrec=200".format(ebsco_profile, ebsco_pass, sf, query, journal))
            #print(call)
            r = requests.get(call)
            tree = ET.ElementTree(ET.fromstring(r.content))
            root = tree.getroot()
            hits = root.find('{http://epnet.com/webservices/SearchService/Response/2007/07/}Hits').text
            log_data = str((query + ',' + sf +',' + journal + ',' + hits)) # send this to a log.
            f = open(log_path, "a")
            f.write(log_data)
            f.write('\n')
            f.close()
            offset = 201
            # only the first 200...need to grab the next x and add to list
            for rec in root.iter('header'):
                uid = rec.attrib['uiTerm']
                if uid not in uids:
                    uids.append(uid)

            while offset <= (math.ceil(int(hits)/200)*200) - 200:
                offset = offset + 200

print("list contains " + str(len(uids)) + " items.")

###################
## Collect metadata from article matches
###################

for i in md_fields.keys():
    headers.append(i)
for i in mv_md_fields.keys():
    headers.append(i)

with open(csv_path, mode='w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    # Write the row data
    for uid in uids:
        metadata = []
        metadata_mv = []
        call = ("https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof={}&pwd={}&query=UI+{}&db=sih".format(ebsco_profile, ebsco_pass, uid))
        r = requests.get(call)
        root = ET.fromstring(r.text)
        for field, query in md_fields.items():
            f = root.findall(query)
            fv = [i.text for i in f]
            metadata.append(fv)
        for field, query in mv_md_fields.items():
            f = root.findall(query)
            fv = [i.text for i in f]
            metadata_mv.append(fv)
        writer.writerow([item for sublist in metadata for item in sublist] + metadata_mv)
