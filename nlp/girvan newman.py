# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:21:32 2019

@author: Athan
"""
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
import community

G = nx.Graph()

G.add_edge("Index","Origo", weight =3.47826087)
G.add_edge("Index","Vs", weight =9.015777611)
G.add_edge("Index","444", weight =20.11291461)
G.add_edge("Index","24.hu", weight =21.80355631)
G.add_edge("Index","Pesti Srácok", weight =2.143622722)
G.add_edge("Index","HVG", weight =13.63216266)
G.add_edge("Origo","Vs", weight =4.025044723)
G.add_edge("Origo","444", weight =8.023535705)
G.add_edge("Origo","24.hu", weight =4.441286196)
G.add_edge("Origo","Pesti Srácok", weight =2.887044388)
G.add_edge("Origo","HVG", weight =3.821899484)
G.add_edge("Vs","444", weight =5.922551253)
G.add_edge("Vs","24.hu", weight =5.385556916)
G.add_edge("Vs","Pesti Srácok", weight =2.444987775)
G.add_edge("Vs","HVG", weight =4.608294931)
G.add_edge("444","24.hu", weight =11.63206872)
G.add_edge("444","Pesti Srácok", weight =1.098901099)
G.add_edge("444","HVG", weight = 10.78582435)
G.add_edge("24.hu","Pesti Srácok", weight =0.865800866)
G.add_edge("24.hu","HVG", weight =12.1434623)
G.add_edge("Pesti Srácok","HVG", weight =3.077651515)

print("links 2015")

print(nx.average_clustering(G,weight="weight"))
part = community.best_partition(G,weight='weight')
part = {'Index': 1, 'Pesti Srácok': 0, 'HVG': 1, 'Origo': 0, 'Vs': 0, '444': 1, '24.hu': 1}
mod = community.modularity(part,G,weight='weight')
print(mod)
part = community.best_partition(G,weight='weight')
mod = community.modularity(part,G,weight='weight')
print(mod)