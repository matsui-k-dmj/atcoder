"""
Binary Indexed Tree（Fenwick Tree） [いかたこのたこつぼ] https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree

a_i に xを加算
a_1 ~ a_i の 和を得る

をO(log n)でできる

"""


class Bit:
    """1-indexなので注意"""

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


# 使用例
# bit = Bit(10)     # 要素数を与えてインスタンス化
# bit.add(2, 10)    # a2に10を加える
# bit.add(5, 5)     # a5に 5を加える
# print(bit.sum(3)) # a1～a3の合計を返す => 10
# print(bit.sum(6)) # a1～a6の合計を返す => 15
# bit.add(3, -6)    # a3に-6を加える
# print(bit.sum(6)) # a1～a6の合計を返す => 9
# print(bit.sum(6) - bit.sum(3))  # a4～a6の合計 => 5


class FenwickTreeInjectable:
    def __init__(self, n, func=lambda x, y: x + y, identity_factory=lambda: 0):
        """
        1-indexなので注意

        Fenwick木では、listやdictなどのオブジェクトを載せることもできる。
        その場合の注意点として、Pythonでは、オブジェクトを特に工夫無くコピーするとインスタンス自体が同じとなる。つまりどれか1つへの反映が他の全てに反映されてしまう。

        それを防ぐため、identity_factory には「引数無しで呼ぶと初期値を生成して返す関数」を与える。これなら毎回別のものが生成される。

        funcは結合法則と単位元の存在を満たせばよい
        funcはadd で idfが listなら、add(2, [534, 10]) とかできる


        """
        self.size = n
        self.tree = [identity_factory() for _ in range(n + 1)]
        self.func = func
        self.idf = identity_factory

    def add(self, i, x):
        tree = self.tree
        func = self.func
        while i <= self.size:
            tree[i] = func(tree[i], x)
            i += i & -i

    def sum(self, i):
        s = self.idf()
        tree = self.tree
        func = self.func
        while i > 0:
            s = func(s, tree[i])
            i -= i & -i
        return s
