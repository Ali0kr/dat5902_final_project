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
y2425 = readInData(fileName,2)
y2425.head()