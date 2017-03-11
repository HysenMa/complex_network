# -*-coding:utf-8-*-
# this python file creates a complex network, and then selects some nodes in two ways
# --MaHaishou
import networkx as nx
import matplotlib.pyplot as plt
import random

__author__ = 'MaHaishou'


# this function select the nodes in the node_list with given sampling rate, then color with blue
def select(sample_rate, node_list):
    select_node = random.sample(node_list, int(float(len(node_list)) * sample_rate))
    # nx.draw_networkx_nodes(G, pos, nodelist=select_node, node_color='b', node_size=10,
    #                       alpha=0.8)  # plot the sampling nodes
    return select_node


G = nx.random_graphs.barabasi_albert_graph(200, 1)  # generate the graph 200 nodes,m=1 BA non scale network
# G = nx.random_graphs.watts_strogatz_graph(200, 4, 0.3)  # 200 nodes 4 neighbors small world network
# G = nx.random_graphs.random_regular_graph(3, 500)  # 200 nodes 3 neighbors random regular network
# G = nx.random_graphs.erdos_renyi_graph(50, 0.2)
pos = nx.spring_layout(G)  # layout of all nodes
# pos = nx.circular_layout(G)
# pos = nx.spectral_layout(G)
# pos = nx.shell_layout(G)

plt.subplot(121)  # first subplot
plt.title("block-random selection")
nx.draw_networkx_edges(G, pos, alpha=0.4)  # plot the edges of G
nx.draw_networkx_nodes(G, pos, node_color='r', node_size=10, alpha=0.8)  # color all nodes with red

block_node1 = []
block_node2 = []
block_node3 = []
block_node4 = []
block_node5 = []
block_node6 = []
block_node7 = []
block_node8 = []
block_node9 = []
sampling_rate = 0.4
num_select = 0

for n in pos.keys():
    if pos[n][0] < 0.3:
        if pos[n][1] < 0.3:
            block_node1.append(n)
        elif pos[n][1] < 0.6:
            block_node2.append(n)
        else:
            block_node3.append(n)
    elif pos[n][0] < 0.6:
        if pos[n][1] < 0.3:
            block_node4.append(n)
        elif pos[n][1] < 0.6:
            block_node5.append(n)
        else:
            block_node6.append(n)
    else:
        if pos[n][1] < 0.3:
            block_node7.append(n)
        elif pos[n][1] < 0.6:
            block_node8.append(n)
        else:
            block_node9.append(n)

num_select = len(block_node1) + len(block_node2) + len(block_node3) + len(block_node4) + len(block_node5) + len(
    block_node6) + len(block_node7) + len(block_node8) + len(block_node9)
# print num_select


select_node1 = select(sampling_rate, block_node1)
select_node2 = select(sampling_rate, block_node2)
select_node3 = select(sampling_rate, block_node3)
select_node4 = select(sampling_rate, block_node4)
select_node5 = select(sampling_rate, block_node5)
select_node6 = select(sampling_rate, block_node6)
select_node7 = select(sampling_rate, block_node7)
select_node8 = select(sampling_rate, block_node8)
select_node9 = select(sampling_rate, block_node9)

select_nodes = select_node1 + select_node2 + select_node3 + select_node4 + select_node5
select_nodes += select_node6 + select_node7 + select_node8 + select_node9

print "block random:", select_nodes

nx.draw_networkx_nodes(G, pos, nodelist=select_nodes, node_color='b', node_size=10,
                       alpha=0.8)  # plot the sampling nodes

plt.subplot(122)  # second subplot
plt.title("random selection")
nx.draw_networkx_edges(G, pos, alpha=0.4)  # plot the edges of G
sampling_node = random.sample(G.nodes(), int(float(G.number_of_nodes()) * sampling_rate))
print "random:", len(sampling_node)
nx.draw_networkx_nodes(G, pos, nodelist=sampling_node, node_color='b', node_size=10,
                       alpha=0.8)  # plot the sampling nodes
other_node = list(set(G.nodes()).difference(set(sampling_node)))
nx.draw_networkx_nodes(G, pos, nodelist=other_node, node_color='r', node_size=10, alpha=0.8)  # plot other nodes

plt.savefig("ba.png")  # save the graph with the format of png
plt.show()
