import matplotlib.pyplot as plt
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import os

#Function to read a specified excel file and sheet number
def readInData (fileName,sheet):
    current_dir = os.getcwd()
    file_dir = current_dir+fileName
    data = pd.read_excel(file_dir,sheet) #Reads in the specified sheet index from the data file
    clean = data.iloc[12::9,[0,3,7,11]] #Takes only the totals from each location and only the male, female and total pass %s 
    clean.columns = ['Location','Male%','Female%','Total%']
    clean = clean.drop(clean[clean['Male%'] == '..'].index)
    clean = clean.drop(clean[clean['Female%'] == '..'].index)
    clean = clean.drop(clean[clean['Total%'] == '..'].index)
    clean = clean.reset_index(drop=True) #Tidies up dataframe by correcting index values
    clean = clean.astype({'Male%':'float','Female%':'float','Total%':'float'})
    return clean

#Function to print max and min values for each column
def maxMinValuesPrint (df):
    maxMale = df[df['Male%']==df['Male%'].max()]
    minMale = df[df['Male%']==df['Male%'].min()]
    maxFemale = df[df['Female%']==df['Female%'].max()]
    minFemale = df[df['Female%']==df['Female%'].min()]
    maxTotal = df[df['Total%']==df['Total%'].max()]
    minTotal = df[df['Total%']==df['Total%'].min()]
    print('Male Max:\n'+str(maxMale)+'\nMale Min:\n'+str(minMale)+'\nFemale Max:\n'+str(maxFemale)+'\nFemale Min:\n'+str(minFemale)+'\nTotal Max:\n'+str(maxTotal)+'\nTotal Min:\n'+str(minTotal))
    return

#Function to return max and min values for each column as a dataframe
def maxMinValuesReturn (df):
    maxMale = df[df['Male%']==df['Male%'].max()]
    maxMale['Index'] = 'maxMale'
    minMale = df[df['Male%']==df['Male%'].min()]
    minMale['Index'] = 'minMale'
    maxFemale = df[df['Female%']==df['Female%'].max()]
    maxFemale['Index'] = 'maxFemale'
    minFemale = df[df['Female%']==df['Female%'].min()]
    minFemale['Index'] = 'minFemale'
    maxTotal = df[df['Total%']==df['Total%'].max()]
    maxTotal['Index'] = 'maxTotal'
    minTotal = df[df['Total%']==df['Total%'].min()]
    minTotal['Index'] = 'minTotal'
    rdf = pd.concat([maxMale,minMale,maxFemale,minFemale,maxTotal,minTotal],axis=0)
    rdf.set_index('Index', inplace = True)
    rdf = rdf.rename_axis(None)
    return rdf

#Creating dataframes, dataframe name is based on final collection date, e.g. 2024-2025 is y25
fileName = '/testcenterdata.xlsx'
y25 = readInData(fileName,2).copy(deep=True)
y24 = readInData(fileName,3).copy(deep=True)
y23 = readInData(fileName,4).copy(deep=True)
y22 = readInData(fileName,5).copy(deep=True)
y21 = readInData(fileName,6).copy(deep=True)
y20 = readInData(fileName,7).copy(deep=True)

#Checking max values for each - remove comment to see raw data
#maxMinValuesPrint(y25)
#maxMinValuesPrint(y24)
#maxMinValuesPrint(y23)
#maxMinValuesPrint(y22)
#maxMinValuesPrint(y21)
#maxMinValuesPrint(y20)

#Processes data using maxMinValueReturn - returns a dataframe with the maximum and minimum pass % locations for males, females and overall
y25c = maxMinValuesReturn(y25)
y24c = maxMinValuesReturn(y24)
y23c = maxMinValuesReturn(y23)
y22c = maxMinValuesReturn(y22)
y21c = maxMinValuesReturn(y21)
y20c = maxMinValuesReturn(y20)

