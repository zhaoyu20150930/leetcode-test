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


def init_g():
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
    return g


def init_back_negtive_g():
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
    g.add('f', ('e', -6))
    g.add('f', ('g', 7))
    g.add('g', ())
    return g
