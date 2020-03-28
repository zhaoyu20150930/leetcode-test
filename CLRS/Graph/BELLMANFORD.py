class G(object):
    def __init__(self):
        self.Adj = {}

    def add(self, v, e):
        if e:
            if v not in self.Adj:
                self.Adj[v] = {e[0]: e[1]}
            else:
                self.Adj[v][e[0]] = e[1]
        else:
            if v not in self.Adj:
                self.Adj[v] = {}
            else:
                self.Adj[v][e[0]] = e[1]


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


def BELLMAN_FORD(G, s):
    INITIALIZE_SINGLE_SOURCE(G.Adj, s)
    for _ in range(1, len(G.Adj.keys())):
        for k in G.Adj.keys():
            for kk in G.Adj[k].keys():
                RELAX(k, kk, G.Adj)
    for k in G.Adj.keys():
        for kk in G.Adj[k].keys():
            if distance[k] > distance[kk] + G.Adj[k][kk]:
                return False
    return True


if __name__ == '__main__':
    g = G()
    g.add('s', ('a', 3))
    g.add('s', ('c', 5))
    g.add('s', ('e', 2))
    g.add('a', ('b', -4))
    g.add('c', ('d', 6))
    g.add('d', ('c', -3))
    g.add('d', ('g', 8))
    g.add('b', ('g', 4))
    g.add('e', ('f', 3))
    g.add('f', ('e', 6))
    g.add('f', ('g', 7))
    g.add('g', ())
    print(BELLMAN_FORD(g, 's'))
