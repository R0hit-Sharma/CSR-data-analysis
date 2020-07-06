import csv
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import math

f1 = open('./DistrictWiseCSRAndADI_2011.csv')
csvFileHandler1 = list(csv.reader(f1))
adiList = []
csrList = []
adi6to10=[]
adi11to14=[]
adi15to18=[]
scale = 100000
for row1 in csvFileHandler1:
	csrList.append(int(row1[11])/scale)
	if int(row1[6]) <= 10 and int(row1[6]) >=6:
		adi6to10.append(int(row1[11])/scale)
	if int(row1[6]) <= 14 and int(row1[6]) >=11:
		adi11to14.append(int(row1[11])/scale)
	if int(row1[6]) <= 18 and int(row1[6]) >=15:
		adi15to18.append(int(row1[11])/scale)
'''
print("6 to 10")
print(str(adi6to10))

print("11 to 14")
print(str(adi11to14))

print("15 to 18")
print(str(adi15to18))
'''
fig, ax = plt.subplots()
plt.xticks(np.arange(min(csrList),max(csrList),max(csrList)/10))

# plot the cumulative histogram for 6 - 10
ax.hist(adi6to10, bins = 1000, normed=True, histtype='step', cumulative=True, label='ADI 6-10', color='red', alpha=0.5, linewidth = 2)

ax.hist(adi11to14, bins = 1000, normed=True, histtype='step', cumulative=True, label='ADI 11-14', color='green', alpha=0.5, linewidth = 2)

ax.hist(adi15to18, bins = 1000, normed=True, histtype='step', cumulative=True, label='ADI 15-18', color='blue', alpha=0.5, linewidth = 2)

# tidy up the figure
ax.grid(True)
ax.legend(loc='lower right')
ax.set_title('CDF for CSR based on ADI 2011')
ax.set_ylabel('Probability')
ax.set_xlabel('CSR Investment (in lakhs)')

plt.show()
