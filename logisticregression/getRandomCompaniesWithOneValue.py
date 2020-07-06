# importing csv module
import csv
import requests
import time
import pandas as pd
import json
from pymongo import MongoClient

df1 = pd.read_csv("./dataForAnalysis1 (copy).csv")
tempDF1 = df1.loc[df1['LocationFlag'] == 1]
tempDF2 = tempDF1.loc['11482':'2585163':116]
df2 = pd.read_csv("./companylocationforanalysis.csv")
print(df2)

if __name__ == '__main__':
	numRows = len(tempDF2['myIndex'])
	for i in range(numRows):
		tempDF2 = df2.loc[df3['District'].isin(tempDF1['District'].tolist())]
		#print(sum(tempDF2['Total'].tolist()),sum(tempDF2['Totalcsr'].tolist()))
		total.append(sum(tempDF2['Total'].tolist()))
		totalCsr.append(sum(tempDF2['Totalcsr'].tolist()))
	df1['Total'] = total
	df1['Totalcsr'] = Totalcsr
	tempDF2.to_csv("./20LatLng.csv")