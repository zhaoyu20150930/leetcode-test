parent = {}
distance = {}


def INITIALIZE_SINGLE_SOURCE(Adj, s):
    for k in Adj.keys():
        distance[k] = float('inf')
        parent[k] = None
    distance[s] = 0


def RELAX(u, v, Adj):
    if distance[v] > distance[u] + Adj[u][v]:
        distance[v] = distance[u] + Adj[u][v]
        parent[v] = u
