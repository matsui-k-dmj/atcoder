"""
非再帰型Segment TreeのPythonによる実装 - Qiita https://qiita.com/dn6049949/items/afa12d5d079f518de368#queryl-r%E3%81%AE%E5%AE%9F%E8%A3%85-1

ある集合Sに対する2項演算子fが次を満たすとき、(S, f)をモノイドという。
(a f b) f c = a f (b f c) # 結合法則
e f a = a f e = a # 単位元の存在

Segment Treeを使うと、数列aiに対して
update(i, x) と 
半開区間 [l, r) に対する、query(l, r) = al f a(l+1) f ... f a(r-1)
がそれぞれ O(log n) で計算できる

# 2 ** (size - 1).bit_length()  # 簡単のため要素数Nを2冪にする について

2^k > N >= 2^(k-1)のとき、Nのビット長はk
<=>
N - 1のビット長は、2^k >= N > 2^(k-1)のとき k

なので 2^k >= N となる最小のkを見つけたいなら、k = (N-1).bit_length() になる。
2^k > N が欲しいなら k = N.bit_length()

# ビット演算
x >> 1 <=> x // 2
"""


class SegmentTree:
    def __init__(self, size, f=lambda x, y: x + y, default=0, initial_list=None):
        """
        初期化処理
        f : SegmentTreeにのせるモノイド
        default : fに対する単位元

        """
        self.size = 2 ** (size - 1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default] * (self.size * 2)  # 要素を単位元で初期化
        self.f = f
        if initial_list is not None:
            for i, v in enumerate(initial_list):
                self.update(i, v)

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i * 2], self.dat[i * 2 + 1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)  # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res
