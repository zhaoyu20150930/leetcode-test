class Node(object):
    def __init__(self, nodes, val=None):
        self.val = val
        self.nodes = nodes


root = Node([])


# TODO 排序查找
def insert(str):
    if not str:
        return
    p = root
    for s in str:
        pns = p.nodes
        for pn in pns:
            if s == pn.val:
                p = pn
                break
        else:
            nn = Node([], s)
            pns.append(nn)
            p = nn


def search(str):
    p = root
    for s in str:
        pns = p.nodes
        for pn in pns:
            if s == pn.val:
                p = pn
                break
        else:
            return False
    return not not str


if __name__ == '__main__':
    insert("hello")
    insert("heoop")
    print(search("heoop"))
