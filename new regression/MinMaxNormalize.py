import csv
import time
import pandas as pd
import json
import ast

df = pd.read_csv('./2.csv')
#df.dropna(inplace = True)
 
def MixMaxNormalized(cellVal, MinVal, MaxVal):
	return (cellVal - MinVal)/(MaxVal - MinVal)

if __name__ == '__main__':
	AmountFinal_Normalized = []
	MarginPer_Normalized = []
	FactoriesFinal_Normalized = []
	ADI_Normalized = []

	mi1 = df['AmountFinal'].min()
	ma1 = df['AmountFinal'].max()

	mi2 = df['Margin %'].min()
	ma2 = df['Margin %'].max()

	mi3 = df['ADI'].min()
	ma3 = df['ADI'].max()

	mi4 = df['FactoriesFinal'].min()
	ma4 = df['FactoriesFinal'].max()

	for i in range(len(df)):
		AmountFinal_Normalized.append(MixMaxNormalized(float(df.iloc[i]['AmountFinal']), float(mi1), float(ma1)))
		MarginPer_Normalized.append(MixMaxNormalized(float(df.iloc[i]['Margin %']), float(mi2), float(ma2)))
		ADI_Normalized.append(MixMaxNormalized(float(df.iloc[i]['ADI']), float(mi3), float(ma3)))
		FactoriesFinal_Normalized.append(MixMaxNormalized(float(df.iloc[i]['FactoriesFinal']), float(mi4), float(ma4)))

	dataDict =  {
			'Constituency':	df['Constituency']
			,'AmountFinal': df['AmountFinal']
			,'state': df['state']
			,'Type':df['Type']
			,'Margin %': df['Margin %']
			,'isMPMinister':df['isMPMinister']
			,'centerAlignment':df['centerAlignment']
			,'stateAlignment':df['stateAlignment']
			,'rs_min_mplad_district':df['rs_min_mplad_district']
			,'is_backward':df['is_backward']
			,'ministry_comp_intersection':df['ministry_comp_intersection']
			,'amount':df['amount']
			,'non_backward':df['non_backward']
			,'not_aligned':df['not_aligned']
			,'Total':df['Total']
			,'Totalcsr':df['Totalcsr']
			,'ADI':df['ADI']
			,'FactoriesFinal':df['FactoriesFinal']
			,'AmountFinal_Normalized':AmountFinal_Normalized
			,'Margin%_Normalized':MarginPer_Normalized
			,'FactoriesFinal_Normalized':FactoriesFinal_Normalized
			,'ADI_Normalized':ADI_Normalized
			}

	DfOut = pd.DataFrame(dataDict)
	DfOut.to_csv('./2_MinMaxNormalized.csv', mode='a', index=False)