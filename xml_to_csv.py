import xml.etree.ElementTree as ET
import pandas as pd
from pandas import DataFrame
import csv
import os

#my_dir = r'C:\Users\tfluhr\Desktop\pquest\pquest_jcira'
my_dir = r'C:\Users\tfluhr\Desktop\pquest_test_2'


for dirs, subs, files in os.walk(my_dir):
    print(subs)
    for f in files:
        my_tree = (dirs + '\\' + f)
        #print("dirs = " + dirs)
        #print("subs = " + subs)
        #print(my_tree)

        #Parse XML file
        tree = ET.parse(my_tree)
        root = tree.getroot()
        
        # start selecting individual items to build list for csv
        
        ids = []
        titles = []
        dois = []
        f_dois = []
        ab = []
        f_ab = []
        keywords = []
        f_keywords = []
        su = []
        f_su = []
        thes= []
        f_thes = []
        naics = []
        f_naics = []
        unclass = []
        f_unclass = []
        date = []
        f_date = []
        volume = []
        f_volume = []
        issue = []
        f_issue = []
        fpage = []
        f_fpage = []
        pcount = []
        f_pcount = []
        dtype = []
        f_dtype = []
        author = []
        f_author = []
        affil = []
        f_affil = []
        cited = []
        f_cited =[]
        # Get RecordID
        
        for rec_id in root.iter('rec'):
                id = str(rec_id.get('recordID'))  
                #print(rec_id.attrib)
                #print(id)
                ids.append (id)
            
        # Get Title   
        for i in root.findall('SearchResults/records/rec/header/controlInfo/artinfo/tig/atl'):
                title = (i.text)
                #print(title)
                titles.append(title)
        
        
        for i in range(1,201):
            dumb_list1 = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/ui[@type="doi"]'
            #print(my_xpath)
            for something in root.findall(my_xpath):
                t_doi = (something.text)
                if t_doi not in dumb_list1:
                    dumb_list1.append(t_doi)
                    dois.append(dumb_list1)    
            f_dois.append(dumb_list1)
        
        for i in range(1,201):
            dumb_list1 = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/ab'
            #print(my_xpath)
            for something in root.findall(my_xpath):
                t_ab = (something.text)
                if t_ab not in dumb_list1:
                    dumb_list1.append(t_ab)
                    ab.append(dumb_list1)    
            f_ab.append(dumb_list1)
        
        for i in range(1,201):
            dumb_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/keyword'
            #print(my_xpath)
            for sub in root.findall(my_xpath):
                term = (sub.text)
                if term not in dumb_list:
                    dumb_list.append(term)
                    keywords.append(dumb_list)    
            f_keywords.append(dumb_list)
        
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/su'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                sub = (i.text)
                if sub not in scratch_list:
                    scratch_list.append(sub)
                    su.append(scratch_list)    
            f_su.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/sug/subj[@type="thes"]'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    thes.append(scratch_list)    
            f_thes.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/sug/subj[@type="naics"]'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    naics.append(scratch_list)    
            f_naics.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/sug/subj[@type="unclass"]'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    unclass.append(scratch_list)    
            f_unclass.append(scratch_list)

        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/pubinfo/dt'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    date.append(scratch_list)    
            f_date.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/pubinfo/vid'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    volume.append(scratch_list)    
            f_volume.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/pubinfo/iid'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    issue.append(scratch_list)    
            f_issue.append(scratch_list)
        
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/ppf'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    fpage.append(scratch_list)    
            f_fpage.append(scratch_list)
        
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/ppct'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    pcount.append(scratch_list)    
            f_pcount.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/doctype'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    dtype.append(scratch_list)    
            f_dtype.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = ('SearchResults/records/rec[' + str(i) + ']/header/controlInfo/refInfo/hasTimesCited')
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = i.get('count')
                if t not in scratch_list:
                    scratch_list.append(t)
                    cited.append(scratch_list)    
            f_cited.append(scratch_list)
            
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/aug/au'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t = (i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    author.append(scratch_list)    
            f_author.append(scratch_list)
            
        
        for i in range(1,201):
            scratch_list = []
            my_xpath = 'SearchResults/records/rec[' + str(i) + ']/header/controlInfo/artinfo/aug/affil'
            #print(my_xpath)
            for i in root.findall(my_xpath):
                t=(i.text)
                if t not in scratch_list:
                    scratch_list.append(t)
                    affil.append(scratch_list)    
            f_affil.append(scratch_list)
            
        ##print(len(ids))
        #print(len(titles))
        #print("dir = " + dirs)
        # merge these lists
        new_lst = [list(x) for x in zip(ids, titles, f_dois, f_ab, f_keywords, f_su, f_thes, f_naics, f_unclass, f_date, f_volume, f_issue, f_fpage, f_pcount, f_dtype, f_author, f_affil, f_cited)]
        
        #print(new_lst[12])
        #print(f_su)
        
        #with open(r'C:\Users\tfluhr\Desktop\test_jm.csv', "w", newline="") as f:
        #    writer = csv.writer(f)
        #    writer.writerows(new_lst)
        
        df = DataFrame(new_lst, columns=['article id', 'title', 'doi', 'abstract', 'keywords', 'subjects', 'thesaurus', 'naics', 'unclass', 'f_date', 'f_volume', 'f_issue', 'f_page', 'f_pcount', 'f_dtype', 'f_author', 'f_affil', 'f_cited'])    
        
        #print(df)
        f = f[:-4]
        results_dir = (dirs[-9:] +"_results" )
        
        final_path = r'C:\Users\tfluhr\Desktop\results_2' + "\\" +  results_dir + "\\" + f + '.csv'
        #print(final_path)
        #print(subs)
        df.to_csv(final_path)
