from CLRS.Graph import init_g
from CLRS.Graph.COMMON import *

S = set()
Q = {}


def EXTRACT_MIN(Q):
    m = float('inf')
    u = ''
    for k, v in Q.items():
        if m > v:
            m = v
            u = k
    return u


def DIJKSTRA(G, s):
    INITIALIZE_SINGLE_SOURCE(G.Adj, s)
    Q = {k: v for k, v in distance.items() if k not in S}
    while Q:
        u = EXTRACT_MIN(Q)
        S.add(u)
        for v in G.Adj[u]:
            RELAX(u, v, G.Adj)
        Q = {k: v for k, v in distance.items() if k not in S}
    return distance


if __name__ == '__main__':
    g = init_g()
    print(DIJKSTRA(g, 's'))
