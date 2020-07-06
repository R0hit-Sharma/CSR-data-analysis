import csv
import scipy.stats as stats
import numpy
import matplotlib.pyplot as plt
import math

f1 = open('./ADI19MappedWith2011DistrictAndGraphDBDistricts2.csv')
csvFileHandler1 = list(csv.reader(f1))
adiList = []
csrList = []

if __name__ == '__main__':
	for row1 in csvFileHandler1:
		if(int(row1[9]) != 0):
			#csrList.append(math.log(int(row1[9]), 10))
			csrList.append(int(row1[9]))
			adiList.append(int(row1[16]))

	print(str(csrList)+'\n'+str(adiList))
	ktau, kp_value = stats.kendalltau(csrList, adiList)
	print('Kendall Correlation')
	print('----------------------------------')
	print('Tau: '+str(ktau)+' , P Value: '+str(kp_value))
	print('----------------------------------')

	stau, sp_value = stats.spearmanr(csrList, adiList)
	print('Spearman Correlation')
	print('----------------------------------')
	print('Tau: '+str(stau)+' , P Value: '+str(sp_value))
	print('----------------------------------')
	
	ptau, _ = stats.pearsonr(csrList, adiList)
	print('Pearson Correlation')
	print('----------------------------------')
	print('Tau: '+str(ptau))
	print('----------------------------------')

	#fig, ax1 = plt.subplots()
	#ax1.plot(csrList, adiList, 'bo')
	#ax = plt.gca()
	#plt.scatter(csrList, adiList)
	#plt.title('Scatter plot ADI-19 vs CSR Investment')
	#plt.ylabel('ADI-19')
	#plt.xlabel('CSR Investment')
	##plt.xscale('log')
	#plt.xticks(numpy.arange(min(csrList),max(csrList),max(csrList)/10))
	#plt.show()#