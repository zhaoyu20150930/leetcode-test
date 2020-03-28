class G(object):
    def __init__(self):
        self.Adj = {}

    def add(self, v, e):
        if v in self.Adj:
            self.Adj[v].append(e)
        else:
            self.Adj[v] = [e, ]


parent = {}

order = []
def DFS_visit(V, Adj, s):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            #拓扑排序
            order.append(v)
            DFS_visit(V, Adj, v)


def DFS(V, Adj):
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(V, Adj, s)


if __name__ == '__main__':
    g = G()
    g.add('s', 'b')
    g.add('s', 'c')
    g.add('b', 's')
    g.add('b', 'f')
    g.add('b', 'e')
    g.add('e', 'b')
    g.add('f', 'b')
    g.add('f', 'c')
    g.add('c', 's')
    g.add('c', 'f')
    g.add('c', 'd')
    g.add('d', 'c')
    DFS(g.Adj.keys(), g.Adj)
    order.reverse()
    print(order)
