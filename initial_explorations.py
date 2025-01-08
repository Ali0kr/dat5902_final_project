import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

#Function to read a specified excel file and sheet number
def readInData (fileName,sheet):
    current_dir = os.getcwd()
    file_dir = current_dir+fileName
    data = pd.read_excel(file_dir,sheet) #Reads in the specified sheet index from the data file
    return data

#Creating dataframes 
fileName = '/testcenterdata.xlsx'
y25 = readInData(fileName,2).copy(deep=True)
y24 = readInData(fileName,3).copy(deep=True)
y23 = readInData(fileName,4).copy(deep=True)
y22 = readInData(fileName,5).copy(deep=True)
y21 = readInData(fileName,6).copy(deep=True)
y20 = readInData(fileName,7).copy(deep=True)

