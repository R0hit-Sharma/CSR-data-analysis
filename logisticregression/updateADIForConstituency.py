# importing csv module
import csv
import requests
import time
import pandas as pd
import json
from pymongo import MongoClient

df = pd.read_csv('./1.csv')
df2 = pd.read_csv("./temp.csv")
if __name__ == '__main__':
	numRows = len(df['Constituency'])
	index = 0
	ADI = []
	couldNotMatch = []
	for i in range(numRows):
		if(df.iloc[i]['Constituency'])
		index = df.iloc[i]['District Code']
		ADI.append(df2.iloc[index]['ADI'])
		print('i: '+str(i)+' Index: '+str(index)+' District name:'+str(df2.iloc[index]['District Name'])+' ADI:'+str(df2.iloc[index]['ADI']))
	df['ADI'] = ADI
	df.to_csv("./dataForAnalysis1.csv")