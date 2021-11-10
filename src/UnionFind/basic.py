class UnionFind:
    def __init__(self, N):
        self.par = [i for i in range(0, N)]
    
    def find(self, x):
        if x != self.par[x]: 
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[y] = x
    
    def same(self, x, y):
        return self.find(self.par[x]) == self.find(self.par[y])

N, Q = map(int, input().split())

uf = UnionFind(N)
for _ in range(0, Q):
    P, A, B = map(int, input().split())
    if P == 0:
        uf.unite(A, B)
    else:
        print("YNeos"[not uf.same(A, B)::2])