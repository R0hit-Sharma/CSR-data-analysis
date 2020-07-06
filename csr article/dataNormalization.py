import csv
import time
import pandas as pd
import json
import ast

df = pd.read_csv('./MinMaxNormalized_DonationAndRelationVariableAdded_SectorWiseCountPerDistrict.csv')
#df.dropna(inplace = True)
 
def MixMaxNormalized(cellVal, MinVal, MaxVal):
	return (cellVal - MinVal)/(MaxVal - MinVal)

if __name__ == '__main__':
	sectorWiseCountPerDistrict_Normalised = []
	


	mi2 = df['sectorWiseCountPerDistrict'].min()
	ma2 = df['sectorWiseCountPerDistrict'].max()

	
	for i in range(len(df)):
		sectorWiseCountPerDistrict_Normalised.append(MixMaxNormalized(float(df.iloc[i]['sectorWiseCountPerDistrict']), float(mi2), float(ma2)))
		print(i)

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
			,'Margin%_Normalized':df['Margin%_Normalized']
			,'ADI_Normalized':df['ADI_Normalized']
			,'sectorWiseCountPerDistrict':df['sectorWiseCountPerDistrict']
			,'political_affiliation_Donation':df['political_affiliation_Donation']
			,'political_affiliation_Relation':df['political_affiliation_Relation']
			,'sectorWiseCountPerDistrict_Normalised':sectorWiseCountPerDistrict_Normalised
			}

	DfOut = pd.DataFrame(dataDict)
	DfOut.to_csv('./dataForAnalysis_SectorCountNormalized.csv', mode='a', index=False)
