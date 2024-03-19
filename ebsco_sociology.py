import requests
import lxml.etree as ET


ebsco_profile = "s5681754.main.eit"
ebsco_pass = "XXXXXXXX"
query_string = "hierarchy"
db_test = "0002-9602"

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

databases= [
    "0002-9602", # American Journal of Sociology
    "0003-1224", # American Sociological Review
    "0037-7732" # Social Forces
]

#call = ("https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof={}&pwd={}&query=SU+{}&db=sih&ISSN={}&numrec=200".format(ebsco_profile, ebsco_pass, query_string, db))

for query in query_strings:
    #call = ("https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof={}&pwd={}&query=SU+{}&db=sih&numrec=200".format(ebsco_profile, ebsco_pass, query))
    #offset = 0
    #batch = 1
    #r = requests.get(call)
    #tree = ET.ElementTree(ET.fromstring(r.content))
    #root = tree.getroot()
    #hits = root.find('{http://epnet.com/webservices/SearchService/Response/2007/07/}Hits').text
    #while offset <= math.ceil(hits/200)*200:
    #print(query, call)
    for sf in search_fields:
        call = ("https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof={}&pwd={}&query={}+{}&db=sih&numrec=200".format(ebsco_profile, ebsco_pass, sf, query))
        offset = 0
        batch = 1
        r = requests.get(call)
        tree = ET.ElementTree(ET.fromstring(r.content))
        root = tree.getroot()
        hits = root.find('{http://epnet.com/webservices/SearchService/Response/2007/07/}Hits').text
        # while offset <= math.ceil(hits/200)*200:
        print(sf + "," + hits + "," + call)


#for rec in root.iter('header'):
#    print(rec.attrib['uiTerm'])

#print(root.nsmap)
#for child in root:
#    print(child.tag, child.text)
# for each database run a query for each search term.  Add article UI to list, if not already in list.

# for each article in list, get metadata
