import numpy as np
import matplotlib.pyplot as plt

#######################################
# Params
#######################################
H=40
max_nodes = 4
neighbor_p = 2.0/max_nodes
B = 1

def gen_graph(max_nodes, neighbor_p):
    nodes = []
    adj   = [[0]]*max_nodes

    for i in range(max_nodes):
        x = 2*B*np.random.rand(2)-B

        nodes.append(x)

        adj[i] = []
        for j in range(max_nodes):
            if not j == i:
                z = np.random.rand()
                if z < neighbor_p:
                    adj[i].append(j)

    return nodes,adj

def graph_to_image(nodes, edges):
    pass

nodes,adj = gen_graph(max_nodes, neighbor_p)
print(nodes)
print(adj)

nodes = np.array(nodes)
plt.figure()
plt.scatter(nodes[:,0],nodes[:,1])

for i in range(max_nodes):
    for j in adj[i]:
        p = nodes[[i,j]]

        plt.plot(p[:,0], p[:,1], color='r')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()
