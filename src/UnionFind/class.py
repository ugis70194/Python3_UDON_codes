UnionFind = type("UnionFind", (),
{
    "__init__": (lambda self, N: setattr(self, "par", [i for i in range(0, N)])),
    "find"    : (lambda self, x: self.par[x] if x != self.par[x] and self.par.__setitem__(x, self.find(self.par[x])) else self.par[x]),
    "unite"   : (lambda self, x, y: self.par.__setitem__(self.find(y), self.find(x))),
    "same"    : (lambda self, x, y: print("YNeos"[self.par[self.find(x)] != self.par[self.find(y)]::2]) ) 
})

N, Q = map(int, input().split())

uf = UnionFind(N)
for _ in range(0, Q):
    P, A, B = map(int, input().split())
    if P == 0:
        uf.unite(A, B)
    else:
        uf.same(A, B)