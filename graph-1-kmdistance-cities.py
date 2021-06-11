import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


data=pd.read_csv(r'C:\Users\Brenda\Documents\distance_potential_regional_hub_nodes.csv')
linkData= pd.DataFrame(data,columns=['source','target','distance'])
print(linkData)

# creating graph G
G = nx.from_pandas_edgelist(linkData, 'source', 'target', True, nx.DiGraph())

print("Nodes of graph: ")
hubs = G.nodes()
print(hubs)

print("Edges of graph: ") 
print(G.edges())

# Drawing the graph
pos = nx.spring_layout(G)

nx.draw(G, pos)

# getting the labels of the node
node_labels = nx.get_node_attributes(G, 'labels')

labels = {} 
   
for node in G.nodes():
    if node in hubs:
        #set the node name as the key and the label as its value 
        labels[node] = node

#Now only add labels to the nodes you require (the hubs in my case)
nx.draw_networkx_labels(G,pos,labels,font_size=16,font_color='r')

# getting the attributes of the edge
edge_labels = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
