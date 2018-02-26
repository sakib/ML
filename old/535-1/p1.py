# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:01:43 2016

@author: vladimir
"""

import random
import numpy as np
from scipy.sparse import lil_matrix
from matplotlib import pyplot as plt
import networkx as nx
from fim import apriori

CCL_OLD = [9, 2, 5, 7, 6, 9, 5, 3, 9, 9, 3, 5, 8, 3]
CCL_NEW = []

sum = 0
for i in range(len(CCL_OLD)):
	CCL_NEW.append(sum)
	sum += CCL_OLD[i]
print(CCL_NEW)

def get_data():
	with open('marketing.data', 'r') as fp:
		data = list(map(lambda line: eval('[' + line.strip() + ']'), 
                filter(lambda line: 'NA' not in line, fp)))
		for i in range(len(data)):
			data[i] = [x+y for (x, y) in list(zip(*[data[i], CCL_NEW]))]
			#print(basket)

		return data

def test_data():
    data = [ [ 1, 2, 3 ], [ 1, 4, 5 ], [ 2, 3, 4 ], [ 1, 2, 3, 4 ],[ 2, 3 ],[ 1, 2, 4 ],[ 4, 5 ],[ 1, 2, 3, 4 ],[ 3, 4, 5 ],[ 1, 2, 3 ] ]
    return data()
   
###############################################################################
# Read data  
###############################################################################
data = get_data()

###############################################################################
# Some basic data analysis
###############################################################################

# Find items list
items = np.unique([item for sublist in data for item in sublist])

# Size of data
N_baskets = len(data)
M_items = len(items)


###############################################################################
# Convert data into vector space format.  We will use a sparse boolean matrix
#   to represent data
###############################################################################
H = lil_matrix((N_baskets,M_items), dtype=np.bool)
for i in range(0,len(data)):
    for j in list(map(int,data[i])):
        H[i,j-1] = True

# Plot this matrix
plt.figure(1)
plt.subplot(121)
plt.spy(H)
plt.title('Vector representation')
plt.xlabel('Items')
plt.ylabel('Baskets')
#plt.show()


###############################################################################
# Convert data into graph format
###############################################################################
"""
g = nx.Graph()
a=['b_'+str(i) for i in range(N_baskets)]
b=['i_'+str(j) for j in range(M_items)]
g.add_nodes_from(a,bipartite=0)
g.add_nodes_from(b,bipartite=1)

i=0
for basket in data:
    for item in basket:
            g.add_edge(a[i], b[list(items).index(item)])
    i+=1

# Draw this graph
pos_a={}
x=0.100
const=0.100
y=1.0
for i in range(len(a)):
    pos_a[a[i]]=[x,y-i*const]

xb=0.500
pos_b={}
for i in range(len(b)):
    pos_b[b[i]]=[xb,y-i*const]

plt.subplot(121)
nx.draw_networkx_nodes(g,pos_a,nodelist=a,node_color='r',node_size=300,alpha=0.8)
nx.draw_networkx_nodes(g,pos_b,nodelist=b,node_color='b',node_size=300,alpha=0.8)

# edges
pos={}
pos.update(pos_a)
pos.update(pos_b)
nx.draw_networkx_edges(g,pos,edgelist=nx.edges(g),width=1,alpha=0.8,edge_color='g')
nx.draw_networkx_labels(g,pos,font_size=10,font_family='sans-serif')

plt.title('Graph representation')
#plt.show()
"""

###############################################################################
# Now do rule finding
###############################################################################

#SUPPORT = -3
#ZMIN = 2
SUPPORT = -0.01*len(data)
ZMIN = 1
#ZMAX = 5
CONF = 80
LIFT = 1.03
ITEMSET_REPORT='a'
#RULES_REPORT='rCL'
RULES_REPORT='C'


#frequent_itemset = apriori(data, supp=SUPPORT, zmin=ZMIN, conf=CONF, eval='l', thresh=LIFT, target='s', report=ITEMSET_REPORT)
frequent_itemset = apriori(data, supp=SUPPORT, zmin=ZMIN, target='s', report=ITEMSET_REPORT)

#rules = apriori(data, supp=SUPPORT, zmin=ZMIN, conf=CONF, eval='l', thresh=LIFT, target='r', report=RULES_REPORT)
rules = apriori(data, supp=SUPPORT, zmin=ZMIN, target='r', report=RULES_REPORT)

#for item in data:
#	print(item)
print('========================')
#for itemset in frequent_itemset: print(itemset)
for i in range(5): print(random.choice(frequent_itemset))
print('------------------------')
#for rule in rules: print(rule)
for i in range(5): print(random.choice(rules))
print('========================')
for rule in rules:
	#print(rule[0])
	if rule[0] < 9 and rule[0] != 1:
		print(rule)

print(len(frequent_itemset))
print(len(rules))
