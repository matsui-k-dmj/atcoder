from functools import reduce


class UnionFind:
    def __init__(self, n):
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
            self.rank[j_root] = self.rank[i_root]
        elif self.rank[i_root] == self.rank[j_root]:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1
            self.rank[j_root] += 1
        else:
            self.parent[i_root] = j_root
            self.rank[i_root] = self.rank[j_root]

        return i

    def isSame(self, i, j):
        return self.findRoot(i) == self.findRoot(j)

    def setGroup(self, elements):
        reduce(self.unite, elements)