import csv
import time
import pandas as pd
import json
import ast

#df = pd.read_csv('./MinMaxNormalized_DonationAndRelationVariableAdded_SectorWiseCountPerDistrict.csv', skiprows=0, nrows=5)
df1 = pd.read_csv('./dataForAnalysis_SectorCountNormalized.csv', skiprows=0, nrows=1148)
df2 = pd.read_csv('./output.csv')
df3 = df2.copy()
df4 = pd.read_csv('./CSR_Final.csv')
#print(df3)
df3['District Code'] = 0
df3['key'] = 0
df3['State'] = 0
df3['LokSabhaConstituency'] = 0
df3['Constituency'] = 0
df3['No'] = 0
df3['Type'] = 0
df3['Winning Candidate'] = 0
df3['Party'] = 0
df3['Electors'] = 0
df3['Votes'] = 0
df3['Turnout'] = 0
df3['Margin'] = 0
df3['Margin %'] = 0
df3['PartyShort'] = 0
df3['isMPMinister'] = 0
df3['LokSabha_Ministry'] = 0
df3['LokSabha_MinCode'] = 0
df3['centerAlignment'] = 0
df3['stateAlignment'] = 0
df3['not_aligned'] = 0
df3['rs_min_name'] = 0
df3['rs_min_ministry'] = 0
df3['rs_mplad_dist'] = 0
df3['is_backward'] = 0
df3['non_backward'] = 0
df3['ministry_comp_intersection'] = 0
df3['invested'] = 0
df3['LocationFlag'] = 0
df3['ADI'] = 0
df3['Margin%_Normalized'] = 0
df3['ADI_Normalized'] = 0
df3['sectorWiseCountPerDistrict'] = 0
df3['political_affiliation_Donation'] = 0
df3['political_affiliation_Relation'] = 0
df3['sectorWiseCountPerDistrict_Normalised'] = 0
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
		idx = df1.index[df1['District'] == df2.iloc[i]['DISTRICT'].upper()].tolist()
		#temp = temp.head(1)
		#idx = temp.index[temp.head(1)]
		#print(idx)
		#print(df1.iloc[idx[0]]['State'])
		if len(idx) > 0:
			df3.loc[i, 'District Code'] = df1.iloc[idx[0]]['District Code']
			df3.loc[i, 'key'] = df1.iloc[idx[0]]['key']
			df3.loc[i, 'State'] = df1.iloc[idx[0]]['State']
			df3.loc[i, 'LokSabhaConstituency'] = df1.iloc[idx[0]]['LokSabhaConstituency']
			df3.loc[i, 'Constituency'] = df1.iloc[idx[0]]['Constituency']
			df3.loc[i, 'No'] = df1.iloc[idx[0]]['No']
			df3.loc[i, 'Type'] = df1.iloc[idx[0]]['Type']
			df3.loc[i, 'Winning Candidate'] = df1.iloc[idx[0]]['Winning Candidate']
			df3.loc[i, 'Party'] = df1.iloc[idx[0]]['Party']
			df3.loc[i, 'Electors'] = df1.iloc[idx[0]]['Electors']
			df3.loc[i, 'Votes'] = df1.iloc[idx[0]]['Votes']
			df3.loc[i, 'Turnout'] = df1.iloc[idx[0]]['Turnout']
			df3.loc[i, 'Margin'] = df1.iloc[idx[0]]['Margin']
			df3.loc[i, 'Margin %'] = df1.iloc[idx[0]]['Margin %']
			df3.loc[i, 'PartyShort'] = df1.iloc[idx[0]]['PartyShort']
			df3.loc[i, 'isMPMinister'] = df1.iloc[idx[0]]['isMPMinister']
			df3.loc[i, 'LokSabha_Ministry'] = df1.iloc[idx[0]]['LokSabha_Ministry']
			df3.loc[i, 'LokSabha_MinCode'] = df1.iloc[idx[0]]['LokSabha_MinCode']
			df3.loc[i, 'centerAlignment'] = df1.iloc[idx[0]]['centerAlignment']
			df3.loc[i, 'stateAlignment'] = df1.iloc[idx[0]]['stateAlignment']
			df3.loc[i, 'not_aligned'] = df1.iloc[idx[0]]['not_aligned']
			df3.loc[i, 'rs_min_name'] = df1.iloc[idx[0]]['rs_min_name']
			df3.loc[i, 'rs_min_ministry'] = df1.iloc[idx[0]]['rs_min_ministry']
			df3.loc[i, 'rs_mplad_dist'] = df1.iloc[idx[0]]['rs_mplad_dist']
			df3.loc[i, 'is_backward'] = df1.iloc[idx[0]]['is_backward']
			df3.loc[i, 'non_backward'] = df1.iloc[idx[0]]['non_backward']
			df3.loc[i, 'ministry_comp_intersection'] = df1.iloc[idx[0]]['ministry_comp_intersection']
			df3.loc[i, 'invested'] = df1.iloc[idx[0]]['invested']
			df3.loc[i, 'LocationFlag'] = df1.iloc[idx[0]]['LocationFlag']
			df3.loc[i, 'ADI'] = df1.iloc[idx[0]]['ADI']
			df3.loc[i, 'Margin%_Normalized'] = df1.iloc[idx[0]]['Margin%_Normalized']
			df3.loc[i, 'ADI_Normalized'] = df1.iloc[idx[0]]['ADI_Normalized']
			df3.loc[i, 'sectorWiseCountPerDistrict'] = df1.iloc[idx[0]]['sectorWiseCountPerDistrict']
			df3.loc[i, 'political_affiliation_Donation'] = df1.iloc[idx[0]]['political_affiliation_Donation']
			df3.loc[i, 'political_affiliation_Relation'] = df1.iloc[idx[0]]['political_affiliation_Relation']
			df3.loc[i, 'sectorWiseCountPerDistrict_Normalised'] = df1.iloc[idx[0]]['sectorWiseCountPerDistrict_Normalised']
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
	df3.to_csv('./outputDistrictVariablesUpdated.csv', mode='w', index=False)
