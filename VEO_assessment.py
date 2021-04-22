#import base modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import openpyxl
import pprint
import csv

#import Global Terrorism Database - all entries 1970-2018
GTD_data = pd.read_csv('/content/globalterrorismdb_0919dist.csv')
#will need to download a copy of the GTD dataset in .csv file format

#check out basic attributes of the database
GTD_data.head()
GTD_data.tail()
GTD_data.shape #-> (191464 instances of 134 attributes)

#value counts of the most common locations (by country) for VEO activity
GTD_data['country_txt'].value_counts()

#value counts for the most common identities (by group name) for VEO activity
GTD_data['gname'].value_counts().head(50)

#create a condensed version; select data only for years 2015-2018
GTD_data_less = GTD_data[GTD_data['iyear'].isin([2015, 2016, 2017, 2018])]
GTD_data_less.head()
GTD_data_less.tail()

#write this new df back out to a .csv file ot save for later
GTD_data_less.to_csv('/content/GTD_data_15-18.csv')

#read in the condensed data set (2015-2018) from the complete GTD dataset
GTD_data = pd.read_csv(f'/content/GTD_data_15-18.csv')

#break out GTD_data by year based in 'iyear' characteristic
GTD_data_2015 = GTD_data[GTD_data['iyear'] == 2015]
GTD_data_2015.name = '2015'
GTD_data_2016 = GTD_data[GTD_data['iyear'] == 2016]
GTD_data_2016.name = '2016'
GTD_data_2017 = GTD_data[GTD_data['iyear'] == 2017]
GTD_data_2017.name = '2017'
GTD_data_2018 = GTD_data[GTD_data['iyear'] == 2018]
GTD_data_2018.name = '2018'
GTD_data_years = [GTD_data_2015, GTD_data_2016, GTD_data_2017, GTD_data_2018]

#clustering - 9 total clusters

#create and empty dictionary to hold the total numbers
cluster_results = {
    '2015' : {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0},
    '2016' : {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0},
    '2017' : {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0},
    '2018' : {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0},
}

groups_list = [
               'Islamic State of Iraq and the Levant (ISIL)',
               'Al-Nusrah Front',
               'Tehrik-i-Taliban Pakistan (TTP)',
               'Khorasan Chapter of the Islamic State',
               'Tripoli Province of the Islamic State',
               'Barqa Province of the Islamic State',
               'Al-Shabaab',
               'Boko Haram',
               'Jamaat Nusrat al-Islam wal Muslimin (JNIM)',
               "New People's Army (NPA)",
               'Abu Sayyaf Group (ASG)',
               'Bangsamoro Islamic Freedom Movement (BIFM)',
               'Al-Qaida in the Arabian Peninsula (AQAP)',
               'Houthi extremists (Ansar Allah)',
               "Donetsk People's Republic",
               "Luhansk People's Republic",
               'Sinai Province of the Islamic State'
]

#pseudocode
#iterate through each year in GTD_data_years
for each in GTD_data_years:
  #return value counts of attacks by group name; turn into a dictionary
  data = dict(each['gname'].value_counts())
  #clean up the dict to assign zero to any group missing from each year
  #iterate through each group in the list
  for group in groups_list:
    #if the .get() method show group not in dict for that year
    if data.get(group) == None:
      #add a value of zero for that group
      data[group] = 0
    else: continue #else continue on to the next group

  #getthe value of each of the 0 clusters from the data
  cluster_1 = data.get('Islamic State of Iraq and the Levant (ISIL)') + data.get('Al-Nusrah Front')
  cluster_2 = data.get('Taliban') + data.get('Khorasan Chapter of the Islamic State')
  cluster_3 = data.get('Tripoli Province of the Islamic State') + data.get('Barqa Province of the Islamic State')
  cluster_4 = data.get('Al-Shabaab')
  cluster_5 = data.get('Boko Haram') + data.get('Jamaat Nusrat al-Islam wal Muslimin (JNIM)')
  cluster_6 = data.get("New People's Army (NPA)") + data.get('Abu Sayyaf Group (ASG)') + data.get('Bangsamoro Islamic Freedom Movement (BIFM)')
  cluster_7 = data.get('Al-Qaida in the Arabian Peninsula (AQAP)') + data.get('Houthi extremists (Ansar Allah)')
  cluster_8 = data.get("Donetsk People's Republic") + data.get("Luhansk People's Republic")
  cluster_9 = data.get('Sinai Province of the Islamic State')

  #dictionary key to assign values to is each.name
  #iterate through each value in the cluster_results dict for that year
  cluster_results.get(each.name)['1'] = cluster_1
  cluster_results.get(each.name)['2'] = cluster_2
  cluster_results.get(each.name)['3'] = cluster_3
  cluster_results.get(each.name)['4'] = cluster_4
  cluster_results.get(each.name)['5'] = cluster_5
  cluster_results.get(each.name)['6'] = cluster_6
  cluster_results.get(each.name)['7'] = cluster_7
  cluster_results.get(each.name)['8'] = cluster_8
  cluster_results.get(each.name)['9'] = cluster_9

pprint.pprint(cluster_results)
