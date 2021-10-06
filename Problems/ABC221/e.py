"""
E - LEQ https://atcoder.jp/contests/abc221/tasks/abc221_e

aの大小関係だけが重要なので、座圧してBITの添え字として使える

BITのライブラリの添え字は1-indexなので注意する

sum_j sum_(0<=i<j)_(ai <= aj) 2^(j-i-1)
sum_j 2^(j-1) sum_(0<=i<j)_(ai <= aj) 2^(-i)
後ろのsumみたいに 二つ比較があって, どっちがが0からなら、BITに追加していて、
前か後ろから操作すればいい。転倒数と考え方は同じ。

BITへの追加とsumのタイミングは端を含むかに依存するからちゃんと考える

1/n % MOD は modinv(n)で求める。そのあとの加算、乗算は普通にできる

1/2^i なら 2^1自体まずpow(2, i, MOD)でもとめる。1/2^1 % MODは modinv(pow(2, i, MOD))
aa^-1 = 1 (mod M) なら (a % M)a^-1 = 1(mod M)なので大丈夫



"""
import sys

# sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

MOD = 998244353
modinv = lambda n: pow(n, MOD - 2, MOD)


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


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # logger.debug("{}".format([]))

    # 座圧
    a2k = {a: k + 1 for k, a in enumerate(sorted(set(a_list)))}  # 1-index for BIT

    bit = FenwickTreeInjectable(N, lambda x, y: (x + y) % MOD, lambda: 0)

    bit.add(a2k[a_list[0]], modinv(pow(2, 0, MOD)))
    s = 0
    for j in range(1, N):
        k = a2k[a_list[j]]
        b = bit.sum(k)  # 1-index
        s = (s + pow(2, j - 1, MOD) * b) % MOD
        bit.add(k, modinv(pow(2, j, MOD)))

    print(s % MOD)


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3
1 2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
3 2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
198495780 28463047 859606611 212983738 946249513 789612890 782044670 700201033 367981604 302538501"""
        output = """830"""
        self.assertIO(input, output)
