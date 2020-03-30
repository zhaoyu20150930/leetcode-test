from CLRS.Graph import *
from CLRS.Graph.COMMON import *


def BELLMAN_FORD(G, s):
    INITIALIZE_SINGLE_SOURCE(G.Adj, s)
    for _ in range(1, len(G.Adj.keys())):
        for k in G.Adj.keys():
            for kk in G.Adj[k].keys():
                RELAX(k, kk, G.Adj)
    print(distance)
    for k in G.Adj.keys():
        for kk in G.Adj[k].keys():
            if distance[kk] > distance[k] + G.Adj[k][kk]:
                return False
    return True


if __name__ == '__main__':
    g = init_back_negtive_g()
    print(BELLMAN_FORD(g, 's'))
