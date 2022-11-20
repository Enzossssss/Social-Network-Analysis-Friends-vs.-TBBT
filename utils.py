# Imported libraries
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Paths
datasets_path = 'datasets/processed datasets/'
images_path = 'output images/'

def visualize_into_a_table(columns, n_rows, tbbt_data, friends_data, table_name):

    rows = [str(i+1) for i in range(n_rows)]
    data = []

    for i in range(n_rows):
        if type(tbbt_data[i][1]) != str:
            data.append([str(tbbt_data[i][0]), str(round(tbbt_data[i][1], 2)), str(friends_data[i][0]), str(round(friends_data[i][1], 2))])
        else:
            data.append([str(tbbt_data[i][0]), str(tbbt_data[i][1]), str(friends_data[i][0]), str(friends_data[i][1])])

    rcolors = plt.cm.BuPu(np.full(len(rows), 0.1))
    ccolors = plt.cm.BuPu(np.full(len(columns), 0.1))
    
    the_table = plt.table(cellText=data,
                        rowLabels=rows,
                        rowColours=rcolors,
                        rowLoc='right',
                        colColours=ccolors,
                        colLabels=columns,
                        loc='center', 
                        cellLoc='left', 
                        colLoc='left', 
                        colWidths= [0.4, 0.2, 0.4, 0.2])
    plt.axis('off')
    plt.savefig(images_path + table_name)
    plt.show()

def visualize_network(g, pos, d, weights, network_names):

    kcores = defaultdict(list)
    n_cores = max(nx.core_number(g).values())
    for n, k in nx.core_number(g).items():
        kcores[k].append(n)

    # compute position of each node with shell layout
    pos = nx.layout.shell_layout(g, list(kcores.values()))


    # draw the graph
    plt.figure(3,figsize=(40,40)) 
    nx.draw(g, pos=pos, nodelist=d.keys(), node_size=[v * 500 for v in d.values()]) # Each node size based on degree
    nx.draw_networkx_labels(g, pos, font_size=20)


    # Modify the width of the edges based to the weigths
    for weight in weights:
            weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in g.edges(data=True) if edge_attr['weight']==weight]
            width = weight*len(g.nodes)*3.0/sum(weights)
            nx.draw_networkx_edges(g,pos,edgelist=weighted_edges,width=width)

    # Save resulting images
    plt.savefig(images_path + network_names)
    plt.show()