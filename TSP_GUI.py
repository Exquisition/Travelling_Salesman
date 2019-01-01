
"""
Graphical visualization for displaying the solution to the TSP

Written By: Andy Zhou
Dec 31, 2018
"""





from TSP_dynamic import *
import PySimpleGUI as sg
import math
import networkx as nx
import numpy as np
import pylab as plt
import string



if __name__ == '__main__':

    randMatrix = initMatrix(12)

    matrix = np.array([[0,2,9,10], [1,0,6,4], [15, 7, 0, 8], [6,3,12,0]])
    min_cost_path = TSP_solve(randMatrix)

    edgelist_min_path = [(min_cost_path[0][i]-1, min_cost_path[0][i+1]-1 ) for i in range(len(min_cost_path[0])-1)]



    G = nx.from_numpy_matrix(randMatrix)

    G = nx.DiGraph(G)

    H = G.edge_subgraph(edgelist_min_path)


    edges = list(H.edges().keys())
    nodes = H.nodes()


    labeldict = {i: "City "+str(i+1) for i in nodes}


    nx.draw(H, labels=labeldict,  with_labels=True, color='-o', edge_color = [ i[2]['weight'] for i in H.edges(data=True) ], edge_cmap=plt.cm.Blues)
    plt.show()
    

