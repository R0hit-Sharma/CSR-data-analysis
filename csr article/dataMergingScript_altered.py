import csv
import time
import pandas as pd
import json
import ast

#df = pd.read_csv('./MinMaxNormalized_DonationAndRelationVariableAdded_SectorWiseCountPerDistrict.csv', skiprows=0, nrows=5)
df1 = pd.read_csv('./factory_urb_model.csv', skiprows=0)
df2 = pd.read_csv('./output.csv')
df3 = df2.copy()
df4 = pd.read_csv('./CSR_Final.csv')
#print(df3)
df3['State'] = 0
df3['Constituency'] = 0
df3['Type'] = 0
df3['Margin'] = 0
df3['isMPMinister'] = 0
df3['centerAlignment'] = 0
df3['stateAlignment'] = 0
df3['not_aligned'] = 0
df3['rs_min_mplad_district'] = 0
df3['is_backward'] = 0
df3['non_backward'] = 0
df3['ministry_comp_intersection'] = 0
df3['ADI'] = 0
df3['AmountFinal'] = 0
df3['FactoriesFinal'] = 0
df3['csrAmountInvested'] = 0
#df.dropna(inplace = True)
#print(df1['District Code'])
#print(df1.District.unique())
#print(df2.DISTRICT.unique())
districtsList = df2.DISTRICT.unique()

def updatePoliticalAndDevelopmentVariables():
	i = 0
	idx = 0
	while i < df3.shape[0]:
		print(i)
		print('------------------------------')
		idx = df1.index[df1['Constituency'] == df2.iloc[i]['DISTRICT'].upper()].tolist()
		#temp = temp.head(1)
		#idx = temp.index[temp.head(1)]
		#print(idx)
		#print(df1.iloc[idx[0]]['State'])
		if len(idx) > 0:
			df3.loc[i, 'State'] = df1.iloc[idx[0]]['State']
			df3.loc[i, 'Constituency'] = df1.iloc[idx[0]]['Constituency']
			df3.loc[i, 'Type'] = df1.iloc[idx[0]]['Type']
			df3.loc[i, 'Margin'] = df1.iloc[idx[0]]['Margin']
			df3.loc[i, 'isMPMinister'] = df1.iloc[idx[0]]['isMPMinister']
			df3.loc[i, 'centerAlignment'] = df1.iloc[idx[0]]['centerAlignment']
			df3.loc[i, 'stateAlignment'] = df1.iloc[idx[0]]['stateAlignment']
			df3.loc[i, 'not_aligned'] = df1.iloc[idx[0]]['not_aligned']
			df3.loc[i, 'rs_min_mplad_district'] = df1.iloc[idx[0]]['rs_min_mplad_district']
			df3.loc[i, 'is_backward'] = df1.iloc[idx[0]]['is_backward']
			df3.loc[i, 'non_backward'] = df1.iloc[idx[0]]['non_backward']
			df3.loc[i, 'ministry_comp_intersection'] = df1.iloc[idx[0]]['ministry_comp_intersection']
			df3.loc[i, 'AmountFinal'] = df1.iloc[idx[0]]['AmountFinal']
			df3.loc[i, 'FactoriesFinal'] = df1.iloc[idx[0]]['FactoriesFinal']
			df3.loc[i, 'ADI'] = df1.iloc[idx[0]]['ADI']
		i = i+1
	return 1

def updateCSRData():
	i=0
	idx = 0
	while i < df3.shape[0]:
		print(i)
		print('------------------------------')
		temp = df4[df3.iloc[i]['DISTRICT'].upper() == df4['DISTRICT']]
		idx = temp.index[df3.iloc[i]['CIN'] == temp['CIN']].tolist()
		if len(idx) > 0:
			#print(temp[df3.iloc[i]['CIN'] == temp['CIN']])
			#print(temp['AMOUNT'][df3.iloc[i]['CIN'] == temp['CIN']].tolist())
			df3.loc[i, 'csrAmountInvested'] = sum(temp['AMOUNT'][df3.iloc[i]['CIN'] == temp['CIN']].tolist())
		i = i + 1
	return 1
if __name__ == '__main__':
	updatePoliticalAndDevelopmentVariables()
	updateCSRData()
	df3.to_csv('./outputDistrictVariablesUpdated_altered.csv', mode='w', index=False)



























	
	
