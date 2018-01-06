import csv
import pandas as pd
import os
print("Processing of input begins")
#read the input file
inputfilepath=os.path.join("..","raw_data","input","zip_to_zcta_2017.xlsx")
zip1=pd.read_excel(inputfilepath)
print("Details of zip1 ",zip1.head())

#Modify  df with required columns
zip1=zip1[["ZIP_CODE","ZCTA"]]
print("Details of modified zip1 ",zip1.head())

print("Processing Census File")
Censusfilepath=os.path.join("..","raw_data","input","Census.csv")
census=pd.read_csv(Censusfilepath)
census.columns=["ZCTA","Population"]
print("Details of census ",census.head())

print("Merging the population ,zipcode and zcta")
new_census=zip1.merge(census,how='inner')
print("Details of new_census ",new_census.head())

#set output path and save to csv
outputfilepath=os.path.join("..","raw_data","output","fipstostate.csv")
new_census.to_csv(outputfilepath)
print("Successfully Completed")