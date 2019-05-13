# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:00:34 2019

@author: Athan
"""

import matplotlib.pyplot as plt
import networkx as nx
 
 
def plot_weighted_graph():
    "Plot a weighted graph"
    #2. Add nodes
    G = nx.Graph() #Create a graph object called G
    node_list = ['444','HVG','Pesti Srácok','   Origo','Vs','Index','24.hu']
    for node in node_list:
        G.add_node(node)
 
    #Note: You can also try a spring_layout
    pos=nx.circular_layout(G) 
    nx.draw_networkx_nodes(G,pos,node_color='green',node_size=1)
 
    #3. If you want, add labels to the nodes
    labels = {}
    for node_name in node_list:
        labels[str(node_name)] =str(node_name)
    nx.draw_networkx_labels(G,pos,labels,font_size=16)
 
 
    #4. Add the edges (4C2 = 6 combinations)
    #NOTE: You usually read this data in from some source
    #To keep the example self contained, I typed this out
    G.add_edge("Pesti Srácok","Vs", weight =0.4)
    G.add_edge("Pesti Srácok","   Origo", weight =0.5)
    G.add_edge("Pesti Srácok","444", weight =0.51)
    G.add_edge("Pesti Srácok","Index", weight =0.52)
    G.add_edge("Pesti Srácok","24.hu", weight =0.53)
    G.add_edge("Pesti Srácok","HVG", weight =0.5)
    G.add_edge("Vs","   Origo", weight =0.28)
    G.add_edge("Vs","444", weight =0.37)
    G.add_edge("Vs","Index", weight =0.33)
    G.add_edge("Vs","24.hu", weight =0.43)
    G.add_edge("Vs","HVG", weight =0.43)
    G.add_edge("   Origo","444", weight =0.32)
    G.add_edge("   Origo","Index", weight =0.32)
    G.add_edge("   Origo","24.hu", weight =0.37)
    G.add_edge("   Origo","HVG", weight =0.39)
    G.add_edge("444","24.hu", weight =0.55)
    G.add_edge("444","Index", weight =0.52)
    G.add_edge("444","HVG", weight = 0.54)
    G.add_edge("Index","24.hu", weight =0.55)
    G.add_edge("Index","HVG", weight =0.54)
    G.add_edge("24.hu","HVG", weight =0.59)
     
    all_weights = []
    #4 a. Iterate through the graph nodes to gather all the weights
    for (node1,node2,data) in G.edges(data=True):
        all_weights.append(data['weight']) #we'll use this when determining edge thickness
 
    #4 b. Get unique weights
    unique_weights = list(set(all_weights))
 
    #4 c. Plot the edges - one by one!
    for weight in unique_weights:
        #4 d. Form a filtered list with just the weight you want to draw
        weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['weight']==weight]
        #4 e. I think multiplying by [num_nodes/sum(all_weights)] makes the graphs edges look cleaner
        width = weight*len(node_list)*3.0/sum(all_weights)
        nx.draw_networkx_edges(G,pos,edgelist=weighted_edges,width=width)
 
    #Plot the graph
    plt.axis('off')
    plt.title('''Text similarity be newsite in 2018
              ''')
    plt.savefig("chess_legends.png") 
    plt.show() 
 
#----START OF SCRIPT
if __name__=='__main__':
    plot_weighted_graph()