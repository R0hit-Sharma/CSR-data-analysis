import pandas as pd
import numpy as np 
import csv
import traceback
f2 = open('./error.txt','w')
df1 = pd.read_csv('dataForAnalysis1_MinMaxNormalized_DonationAndRelationVariableAdded_Refined.csv')
print(df1)
#df1 = df1.drop('Unnamed: 0',1)
df3 = df1.copy()
df3['sectorWiseCountPerDistrict']=0
df2 = df1[df1['invested']==1]
print(df2.shape)
sectorList = df2['buss_sector'].unique()
districtList = df2['District'].unique()
dict1 = df2.groupby(['District','buss_sector']).size()
print(dict1)
i=0
while i < df3.shape[0]:
	#print(i)
	try:
		#x = df3.iloc[i]['District']
		#y = df3.iloc[i]['buss_sector']
		#print(x,y,type(y))
		value = dict1[df3.iloc[i]['District']][df3.iloc[i]['buss_sector']]
		#print(value)
	except KeyError:
		value = 0
	except TypeError:
		value = 0
	df3.loc[i,'sectorWiseCountPerDistrict'] = value
	i=i+1
#df3.to_csv('./MinMaxNormalized_DonationAndRelationVariableAdded_SectorWiseCountPerDistrict.csv', index=False)
#print(df3[df3['invested']==1])
'''
df2 = pd.read_csv('./MinMaxNormalized_SectorWiseCountPerDistrict.csv')
df3 = df1.copy()
df3['political_affiliation_Relation']=0

count = 0
matchcount = 0
desiredcount = 0
i= 0
while i < len(df1) :
	count = count + 1
	for j in range(len(df2)):
		if df1.iloc[i]['CIN'] == df2.iloc[j]['CIN']:
			matchcount = matchcount+1
			if df1.iloc[i]['Party'] == df2.iloc[j]['PPNAME'] :
				df3.loc[i,'political_affiliation_Relation'] = 1
				#print('match')
				desiredcount = desiredcount + 1
	#print('count'+str(count))
	#print(df1.iloc[i]['CIN'] + df1.iloc[i]['company'])
	#print('matchcount'+str(matchcount))	
	#print('desiredcount'+str(desiredcount))
	if matchcount == 0:	
		i=i+1148
	else :
		i = i+1
	matchcount = 0
	print(i)
df3.to_csv('./dataForAnalysis1_MinMaxNormalized_DonationAndRelationVariableAdded.csv', index=False)
'''
'''
df1 = pd.read_csv('./dataForAnalysis1_MinMaxNormalized_DonationAndRelationVariableAdded.csv')
print('Relation: '+str(df1['political_affiliation_Relation'].sum()))
print('Donation: '+str(df1['political_affiliation_Donation'].sum()))
positiveDf = df1[df1['invested']==1]
print('No of instances of CSR investment: '+str(len(positiveDf)))
print('No of unique Companies which have done CSR : '+str(len(positiveDf['CIN'].unique())))
print('Invested = 1, Relation: '+str(positiveDf['political_affiliation_Relation'].sum()))
print('Invested = 1, Donation: '+str(positiveDf['political_affiliation_Donation'].sum()))
'''
