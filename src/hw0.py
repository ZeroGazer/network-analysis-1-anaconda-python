import numpy as np
import networkx as nx
import operator

data = np.loadtxt('facebook_combined.txt')  # load all the edges, which is saved
                                            # in facebook_combined.txt file
data = data.astype(int)   # conver nodeid from float to int, like 1.0 to 1
#print data.shape

edges_list = map(tuple, data)  # map(function, iterable): apply function to
                               # every item of iterable and return a list of
                               # results
#print edges_list[:10]

fbG = nx.Graph(edges_list)  # generate the facebook graph

# print number of nodes and edges, and whether this network is connected or not
print 'Number of nodes: ' + str(nx.number_of_nodes(fbG))
print 'Number of edge: ' + str(nx.number_of_edges(fbG))
print 'The network is connected: ' + str(nx.is_connected(fbG)) + '\n'

# print the id of node(or nodes) with maximum degree
max_degree_node = max(nx.degree(fbG).iteritems(), key=operator.itemgetter(1))[0]
print ('The id of node(or nodes) with maximum degree: ' + str(max_degree_node)
       + '\n')

# print the clustering coefficient of the previous maximum degree node 
# and average clustering coefficient of the whole graph
print ('The clustering coefficient of the previous maximum degree node: '
       + str(nx.clustering(fbG, max_degree_node)))
print ('The average clustering coefficient of the whole graph: '
       + str(nx.average_clustering(fbG) + '\n'))

# print number of triangles, check networkx.algorithms.cluster.triangles()
# function in networkx document
triangles_list = nx.triangles(fbG)
num_of_triangles = 0
for key in triangles_list.keys():
    num_of_triangles += triangles_list[key]
num_of_triangles /= 3
print 'Number of triangles: ' + str(num_of_triangles) + '\n'

# print the shortest path from node 5 to 3000
shortest_path_list = nx.shortest_path(fbG, 5, 3000)
print 'The shortest path from node 5 to 3000'
for nodes in shortest_path_list:
    print '\t' + str(nodes)
print '\n'

# print the diameter and average shortest path length, it may take several
# minutes to complete, BE PATIENT!
print 'The diameter: ' + str(nx.diameter(fbG)) + '\n'
print ('The average shortest path length: '
       + str(nx.average_shortest_path_length(fbG)) + '\n')
