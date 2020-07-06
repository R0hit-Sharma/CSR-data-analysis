import csv
from py2neo import Graph, Node, Relationship, authenticate
import sys
from datetime import datetime

username="neo4j"
password="neo4j"
server = "10.237.27.115"
port="7474"
con_url = 'http://'+username+':'+password+'@'+server+':'+port+'/db/data/'
graph=Graph(con_url)

#graph = Graph(ip_addr = "http://localhost:7474/", username = "neo4j", password = "neo4j")
epoch = datetime(1970,1,1)

def DonatedTo():
	f1 = open("./newDonationData.csv")

	csv_f1 = csv.reader(f1)

	max_id = graph.run("MATCH ()-[r]->() RETURN max (r.relid)").data()
	int_max_id = max_id[0][u'max (r.relid)']
		
	f2 = open('./not_in_gdb.csv','w')

	csv_f2 = csv.writer(f2, delimiter=',')

	count = 0
	for row1 in csv_f1:
		int_max_id = int_max_id+1
		temp = datetime(int(row1[2]),1,1)

		delta_time = (temp - epoch).total_seconds()
		stored_id = graph.run("match (c:company),(p:politicalparty) where c.cin = '"+row1[4]+"' and p.uuid = "+row1[3]+" create (c)-[r:donatedto{amount: "+row1[1]+", year: '"+str(int(delta_time))+"', relid: "+ str(int_max_id)+"}]->(p) return r.relid").data()
		try:
			int_stored_id = stored_id[0][u'r.relid']
			count = count+1
		except:
			s = row1[0]+','+ row1[1]+','+ row1[2]+','+ row1[3]+','+ row1[4]
			row = [s]
			csv_f2.writerow(row)
			
	print("# of donatedto relationships created: "+str(count))
	return 0
	
def WorksIn():
	p = '%d/%m/%Y'
	
	f1 = open("./DirectorsofCompaniesNotInGraphDB.csv")
	csv_f1 = csv.reader(f1)
	max_id = graph.run("MATCH ()-[r]->() RETURN max (r.relid)").data()
	int_max_id = max_id[0][u'max (r.relid)']
		
	f2 = open('./CouldNotMakeWorksInRelation.csv','w')
	csv_f2 = csv.writer(f2, delimiter=',')

	count = 0
	for row1 in csv_f1:
		int_max_id = int_max_id+1
		temp = str(row1[3])
		
		delta_time = (datetime.strptime(temp, p) - epoch).total_seconds()
		
		stored_id = graph.run("match (c:company),(b:businessperson) where c.cin = '"+row1[6]+"' and b.din = '"+str(row1[1])+"' create (b)-[r:worksin{bidirectional: false, relid: "+str(int_max_id)+", enddate: 0, iscurrent: true, designation: 'Director', startdate: '"+str(int(delta_time))+"' }]->(c) return r.relid").data()
		try:
			int_stored_id = stored_id[0][u'r.relid']
			count = count+1
		except:
			s = row1[0]+','+ row1[1]+','+ row1[2]+','+ row1[3]+','+ row1[4]+','+ row1[5]
			row = [s]
			csv_f2.writerow(row)
			
	print("# of worksin relationships created: "+str(count))
	return 0
	
def DeleteRel():
	for relid in range(605313, 605658):
		graph.run("MATCH ()-[r:worksin]->() where r.relid = "+str(relid)+" delete r")
	return 0

def factoryLocatedAt():
	f1 = open("./temp.csv")
	csv_f1 = csv.reader(f1)
	max_id = graph.run("MATCH ()-[r]->() RETURN max (r.relid)").data()
	int_max_id = max_id[0][u'max (r.relid)']
		
	f2 = open('./CouldNotMakeRelation.csv','w')
	csv_f2 = csv.writer(f2, delimiter=',')

	count = 0
	for row1 in csv_f1:
		if(row1[7]!=''):
			print(row1[7])
			int_max_id = int_max_id+1
			#temp = str(row1[3])
				
			stored_id = graph.run("match (c:company),(d:district) where c.cin = '"+row1[0]+"' and (d.name = '"+str(row1[7])+"' OR '"+str(row1[7])+"' in d.aliases) create (c)-[r:factoryLocatedAt{bidirectional: false, relid: "+str(int_max_id)+", type: '"+str(row1[2])+"' }]->(d) return r.relid").data()
			try:
				int_stored_id = stored_id[0][u'r.relid']
				count = count+1
			except:
				#s = row1[0]+','+ row1[7]+','+ row1[2]
				#row = [s]
				csv_f2.writerow(row1)
			
	print("# of factoryLocatedAt relationships created: "+str(count))
	return 0
	
if __name__ == '__main__':
	if len (sys.argv) == 1 :
		print('Argument Expected')
	else:
		if sys.argv[1] == '1':
			print('DonatedTo')
			DonatedTo()
		elif sys.argv[1] == '2':
			print('WorksIn')
			WorksIn()
		elif sys.argv[1] == '3':
			print('DeleteRel')
		elif sys.argv[1] == '4':
			print('factoryLocatedAt')
			factoryLocatedAt()
		else:
			print('Incorrect Argument')
	
	
