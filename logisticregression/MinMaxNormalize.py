import csv
import time
import pandas as pd
import json
import ast

df = pd.read_csv('./dataForAnalysis1.csv')
#df.dropna(inplace = True)
 
def MixMaxNormalized(cellVal, MinVal, MaxVal):
	return (cellVal - MinVal)/(MaxVal - MinVal)

if __name__ == '__main__':
	MarginPer_Normalized = []
	ADI_Normalized = []


	mi2 = df['Margin %'].min()
	ma2 = df['Margin %'].max()

	mi3 = df['ADI'].min()
	ma3 = df['ADI'].max()


	for i in range(len(df)):
		MarginPer_Normalized.append(MixMaxNormalized(float(df.iloc[i]['Margin %']), float(mi2), float(ma2)))
		ADI_Normalized.append(MixMaxNormalized(float(df.iloc[i]['ADI']), float(mi3), float(ma3)))

	dataDict =  {
			'company':df['company']
			,'CIN':df['CIN']
			,'buss_sector':df['buss_sector']
			,'sectorCode':df['sectorCode']
			,'ministriesInfluenced':df['ministriesInfluenced']
			,'key':df['key']
			,'District Code':df['District Code']
			,'District':df['District']
			,'State':df['State']
			,'LokSabhaConstituency':df['LokSabhaConstituency']
			,'Constituency':	df['Constituency']
			,'No': df['No']
			,'Type':df['Type']
			,'Winning Candidate': df['Winning Candidate']
			,'Party':df['Party']
			,'Electors':df['Electors']
			,'Votes':df['Votes']
			,'Turnout':df['Turnout']
			,'Margin': df['Margin']
			,'Margin %': df['Margin %']
			,'PartyShort': df['PartyShort']
			,'isMPMinister':df['isMPMinister']
			,'LokSabha_Ministry':df['LokSabha_Ministry']
			,'LokSabha_MinCode':df['LokSabha_MinCode']
			,'centerAlignment':df['centerAlignment']
			,'stateAlignment':df['stateAlignment']
			,'not_aligned':df['not_aligned']
			,'rs_min_name':df['rs_min_name']
			,'rs_min_ministry':df['rs_min_ministry']
			,'rs_mplad_dist':df['rs_mplad_dist']
			,'is_backward':df['is_backward']
			,'non_backward':df['non_backward']
			,'ministry_comp_intersection':df['ministry_comp_intersection']
			,'invested':df['invested']
			,'LocationFlag':df['LocationFlag']
			,'ADI':df['ADI']
			,'Margin%_Normalized':MarginPer_Normalized
			,'ADI_Normalized':ADI_Normalized
			}

	DfOut = pd.DataFrame(dataDict)
	DfOut.to_csv('./dataForAnalysis1_MinMaxNormalized.csv', mode='a', index=False)