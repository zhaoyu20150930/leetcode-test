class G(object):
    def __init__(self):
        self.Adj = {}

    def add(self, v, e):
        if v in self.Adj:
            self.Adj[v].append(e)
        else:
            self.Adj[v] = [e, ]


def BFS(V, Adj, s):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1


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
    BFS(None, g.Adj, 's')
