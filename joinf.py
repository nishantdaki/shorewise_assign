import csv
from os import listdir
from os.path import isfile, join, splitext
import pandas as pd


dat_folder = "./dat/"
csv_folder = "./cs/"

try:
    try:
        with open(join(dat_folder + "DATA.dat")) as datfile:
            df = pd.read_csv(datfile, sep='\t', skip_blank_lines=True)
        with open(join(dat_folder + "DATA1.dat")) as datfile:
            df1 = pd.read_csv(datfile, sep='\t', skip_blank_lines=True)
        dfmain = pd.concat([df,df1])
        print(dfmain)
    finally:
        datfile.close()
    
except FileNotFoundError as e:
    print("data or csv files folder not Found")
except Exception as e:
    print(e)