 
 in the follwing documnt i imported the library like python rapper (psycopg2) and pandas to mainplate the data 
 and from sql_queries i imported every thing.
 '''import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *'''


here is build connection to database sparkifydb and calling cursor object to deal with databace 
"""""conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()
"""""
Here is functinon to list the json files
"""def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files"""


In general "etl.ipynb" is extracting the data from json files and load into tables 

______________________________________________________________________________________
______________________________________________________________________________________


IN sql_queries here building database schema ,create tables and insert values into tables. 

______________________________________________________________________________________

In create_tables  
execute create_table_queries, drop_table_queries from  sql_queries file 

