class SegTree:
    """SegTree
    """
    def __init__(self, N, segfunc, ide, initial_list=None):

        self.ide = ide
        self.segfunc = segfunc

        # 簡単のために要素数を2のべき乗にしておく
        _n = N
        self.n = 1
        while (self.n < _n):
            self.n = self.n * 2

        self.tree = [self.ide for _ in range(2 * self.n - 1)]

        if initial_list is not None:
            for i, v in enumerate(initial_list):
                self.update(i, v)

    def update(self, i, x):
        i = i + self.n - 1
        self.tree[i] = x

        # 親を更新
        while (i > 0):
            i = (i - 1) // 2
            l = self.tree[i * 2 + 1]
            r = self.tree[i * 2 + 2]
            self.tree[i] = self.segfunc(l, r)

    def query(self, l, r):
        """https://proc-cpuinfo.fixstars.com/2017/07/optimize-segment-tree/
        
        Args:
            l (int): 左 inclusive
            r (int): 右 exclusive
        """
        l += (self.n - 1)
        r += (self.n - 1)
        res = self.ide
        while l < r:
            if l & 1 == 0:  # 奇数のとき。l += (self.n - 1)してるから
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1 == 0:
                res = self.segfunc(res, self.tree[r - 1])
                r -= 1

            l = l // 2
            r = r // 2

        return res