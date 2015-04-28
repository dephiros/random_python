import Queue

class Tree:
    def __init__(value):
        self.root = value
        self.children = [] # list of Tree objects

def bfs(tree):
    q = Queue.Queue()
    if not tree: return
    q.put(tree)
    while q.qsize() > 0:
        t = q.get()
        print t.root
        for c in t.children:
            q.put(c)

def dfs(tree):
    if not tree or tree.children: return
    print tree.root
    for t in tree.children:
        dfs(t)
