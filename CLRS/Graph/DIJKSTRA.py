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
S = set()
Q = {}


def INITIALIZE_SINGLE_SOURCE(Adj, s):
    for k in Adj.keys():
        distance[k] = float('inf')
        parent[k] = None
    distance[s] = 0


def RELAX(u, v, Adj):
    if distance[v] > distance[u] + Adj[u][v]:
        distance[v] = distance[u] + Adj[u][v]
        parent[v] = u


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
    g = G()
    g.add('s', ('a', 3))
    g.add('s', ('c', 5))
    g.add('s', ('e', 2))
    g.add('a', ('b', 4))
    g.add('c', ('d', 6))
    g.add('d', ('c', 3))
    g.add('d', ('g', 8))
    g.add('b', ('g', 4))
    g.add('e', ('f', 3))
    g.add('f', ('e', 6))
    g.add('f', ('g', 7))
    g.add('g', ())
    print(DIJKSTRA(g, 's'))
