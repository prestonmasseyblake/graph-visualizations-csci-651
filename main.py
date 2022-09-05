import networkx as nx
import matplotlib.pyplot as plt
from random import random
# g = nx.erdos_renyi_graph(1000, 0.5)

# print(g)
# G10,0.5, 
#G200,0.005, 
# G500,0.05 
def custom_erdos_renyi_graph(size, probability):
    G = nx.Graph()
    for i in range(size):
        G.add_node(i)
    for i in range(size):
        for x in range(i +  1, size):
            if random() < probability:
                G.add_edge(i, x)
            
    print(G)
    
    return G

gg =custom_erdos_renyi_graph(10, .5)
nx.draw(gg)
plt.show()
ggg= custom_erdos_renyi_graph(200, .005)
nx.draw(ggg)
plt.show()
# custom_erdos_renyi_graph(500, .05)




# generate 10 with different sizes 
# .0001
#.0005 

# try to emulate figure from the 3.6 of the book 
# http://networksciencebook.com/chapter/3#evolution-network
#plt.plot 
# we are plotting thte size of the largest connected component 
#len(max(nx.connected_components(gnp(n, p)), key=len))



#6 counting the degree distributions  