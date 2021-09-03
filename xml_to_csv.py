import requests

#batch = 1
#offset = 0

journals = [
"0309-0566",
"0017-8012",
"0019-8501",
"0265-0487",
"0167-8116",
"0265-1335",
"0091-3367",
"0021-8499",
"0022-0078",
"1472-0817",
"0736-3761",
"1057-7408",
"0093-5301",
"1094-9968",
"0262-1703",
"0022-2429",
"2333-6080",
"0022-2437",
"0743-9156",
"0022-4359",
"0887-6045",
"0965-254X",
"0092-0703",
"0263-4503",
"0923-0645",
"0732-2399",
"1470-5931",
"0742-6046",
"1570-7156",
]

journals_other = [
#"1069-031X", #"0262-1703", ,
"0263-4503", # psych dbname,
#"0267-257X", #"2333-6080", 
#"0092-0703",  #something weird
]

for i in journals_other:
    offset = 0
    batch = 1
    while offset <= 20200:
        print(i)    
        api_call = ('https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof=s8989826.main.eitws&pwd=xxxxxxx&query=IS+%s&db=bth&numrec=200' % i)
        save_dir = ('C:\\Users\\tfluhr\\Desktop\\pquest_test_2\\%s\\' % i)
        off_plus = offset + 1
        call = (api_call  + '&startrec=' + str(off_plus))
        print('batch ' + str(batch))
        print('offset ' + str(offset))
        batch+=1
        offset = offset + 200
        
        write_url = (save_dir + str(batch) + '.xml' )
        #print(write_url)
        
        response = requests.get(call)
        with open(write_url, 'wb') as file:
            file.write(response.content)

