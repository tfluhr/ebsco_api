import os
import glob
import pandas as pd

my_dir = r'C:\Users\tfluhr\Desktop\results_2'

for dirs, subs, files in os.walk(my_dir):
    for i in subs:
        os.chdir(r'C:\Users\tfluhr\Desktop\results_2' + "\\" + i)
        #print(r'C:\Users\tfluhr\Desktop\results' + "\\" + i)

        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        
        #combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        #export to csv
        combined_csv.to_csv( i + "_csv.csv", index=False, encoding='utf-8-sig')
