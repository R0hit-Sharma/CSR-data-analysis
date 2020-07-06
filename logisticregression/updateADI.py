# importing csv module
import csv
import requests
import time
import pandas as pd
import json
from pymongo import MongoClient

f1 = open("./index.csv")
df = pd.read_csv('./dataForAnalysis1(copy).csv')
df2 = pd.read_csv("./districtsForRunningUpdateADIScript.csv")

if __name__ == '__main__':
	index = 0
	numRows = len(df['District Code'])
	ADI = []
	couldNotMatch = []
	for i in range(numRows):
		index = df.iloc[i]['District Code']
		ADI.append(df2.iloc[index]['ADI'])
		print('i: '+str(i)+' Index: '+str(index)+' District name:'+str(df2.iloc[index]['District Name'])+' ADI:'+str(df2.iloc[index]['ADI']))
	df['ADI'] = ADI
	df.to_csv("./dataForAnalysis1.csv")