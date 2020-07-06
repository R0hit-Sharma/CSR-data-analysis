# importing csv module
import csv
import requests
import time
import pandas as pd
import json
from pymongo import MongoClient
import ast

df1 = pd.read_csv("./1.csv")#linear regression dta to be updated
df2 = pd.read_csv('./2.csv')#constituency to district mapping
df3 = pd.read_csv('./3.csv')#csr data district wise

#print(df1.iloc[index]['Constituency'])
#name = ['ANDAMAN AND NICOBAR']
#df2.dropna(inplace = True)
#tempDF1 = df2.loc[df2['Constituency'].isin(name)]
#print(tempDF1['District'].tolist())
#tempDF2 = df3.loc[df3['District'].isin(tempDF1['District'].tolist())]
#print(sum(tempDF2['Total'].tolist()),sum(tempDF2['Totalcsr'].tolist()))
#df1['Total'] = sum(tempDF2['Total'].tolist())
#df1['Totalcsr'] = sum(tempDF2['Totalcsr'].tolist())
df2.dropna(inplace = True)
if __name__ == '__main__':
	total = []
	totalCsr = []
	numRows = len(df1['Constituency'])
	for i in range(numRows):
		name = "['"+df1.iloc[i]['Constituency']+"']"
		tempDF1 = df2.loc[df2['Constituency'].isin(ast.literal_eval(name))]
		#print(tempDF1['District'].tolist())
		tempDF2 = df3.loc[df3['District'].isin(tempDF1['District'].tolist())]
		#print(sum(tempDF2['Total'].tolist()),sum(tempDF2['Totalcsr'].tolist()))
		total.append(sum(tempDF2['Total'].tolist()))
		totalCsr.append(sum(tempDF2['Totalcsr'].tolist()))
	df1['Total'] = total
	df1['Totalcsr'] = totalCsr
	df1.to_csv("./1.csv")