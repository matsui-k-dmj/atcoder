from functools import reduce
from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.N = n
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def findRoot(self, i):
        if self.parent[i] == i:  # 親が自分ならroot
            return i
        else:
            self.parent[i] = self.findRoot(self.parent[i])  # 親をrootに付け替える
            return self.parent[i]

    def unite(self, i, j):
        i_root = self.findRoot(i)
        j_root = self.findRoot(j)
        if i_root == j_root:
            return

        if self.rank[i_root] > self.rank[j_root]:  # ランクが高い方を親にする。
            self.parent[j_root] = i_root
        elif self.rank[i_root] == self.rank[j_root]:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1
        else:
            self.parent[i_root] = j_root

        return i

    def isSame(self, i, j):
        return self.findRoot(i) == self.findRoot(j)

    def setGroup(self, elements):
        reduce(self.unite, elements)

    def getElementCount(self):  # 要素ごとにそれが属してる集合の要素数を取る
        roots = [self.findRoot(i) for i in range(self.N)]
        counts = Counter(roots)
        return [counts[r] for r in roots]

    def getRootCount(self):  # ルートごとにそれが属してる集合の要素数を取る
        roots = [self.findRoot(i) for i in range(self.N)]
        counts = Counter(roots)
        return counts