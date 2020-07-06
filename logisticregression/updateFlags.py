# importing csv module
import csv
import requests
import time
import pandas as pd
import json
from pymongo import MongoClient

f1 = open("./index.csv")
#f2 = open("./dataForAnalysis (copy).csv")
df = pd.read_csv("./dataForAnalysis (copy).csv")
#f3 = open("./dataForAnalysis1.csv",mode= 'w')

#csv_f1 = list(csv.reader(f1))
df2 = pd.read_csv('./index.csv')
#csv_f2 = list(csv.reader(f2))
#csv_f3 = csv.writer(f3,delimiter=',')


if __name__ == '__main__':
	index = 0
	count=0
	numRows = len(df['company'])
	flags = []
	#print('-----------------------')
	#print(df2.iloc[0]['myIndex'])
	#print(df.iloc[2]['myIndex'] +'compared with'+ df2.iloc[0]['myIndex'])
	#print('-----------------------')
	for i in range(numRows):
		if(df.iloc[i]['myIndex'] == df2.iloc[index]['myIndex']):
			flags.append('1')
			print('Matched '+str(df2.iloc[index]['myIndex']))
			index = index + 1
			count = count + 1
		else:
			flags.append('0')
		#print(str(i))
	print('------------------')
	print(str(count))
	print('------------------')
	df['LocationFlag'] = flags
	df.to_csv("./dataForAnalysis1.csv")
	'''
	for row2 in csv_f2:
		if(row2[0] == csv_f1[index]):
			flag = 1
			index = index+1
		else:
			flag = 0
		count = count + 1
		#print(str(count)+':'+str(flag))
		#f3.write(row2[0]+','+row2[1]+','+row2[2]+','+row2[3]+','+row2[4]+','+row2[5]+','+row2[6]+','+row2[7]+','+row2[8]+','+row2[9]+','+row2[10]+','+row2[11]+','+row2[12]+','+row2[13]+','+row2[14]+','+row2[15]+','+row2[16]+','+row2[17]+','+row2[18]+','+row2[19]+','+row2[20]+','+row2[21]+','+row2[22]+','+row2[23]+','+row2[24]+','+row2[25]+','+row2[26]+','+row2[27]+','+row2[28]+','+row2[29]+','+row2[30]+','+row2[31]+','+row2[32]+','+row2[33]+','+row2[34]+','+row2[35]+','+row2[36]+','+str(flag)+'\n')
		#row2.append(flag)
		f3.write(str(flag))
	'''