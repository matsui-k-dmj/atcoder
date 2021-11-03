"""
区間スケジューリング

Pythonのfractions.Fractionは遅いので使えないし、分母0にも対応してない。
カスタムクラスを使う。

二つ以上の要素のソートは遅いので、必要が無ければ、別々のリストで管理して、
argsort
    i_list = sorted(range(len(a_list)), key=lambda i: a_list[i])
を使う。

"""

import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from math import gcd


class Fraction:
    __slots__ = ["a", "b"]

    ##入力定義
    def __init__(self, Numerator=0, Denominator=1, expanded=True, reduction=False):
        """分数のオブジェクトを生成する.

        Numerator: 分子
        Denominator: 分母 (!=0)

        expanded 分母 == 0を許容する
        """
        assert Denominator or expanded, "分母が0"

        if Denominator < 0:
            Numerator *= -1
            Denominator *= -1

        self.a = Numerator
        self.b = Denominator
        if reduction:
            g = gcd(Numerator, Denominator)
            self.a = Numerator // g
            self.b = Denominator // g

    # 表示定義
    def __str__(self):
        if self.b == 1:
            return str(self.a)
        else:
            return "{}/{}".format(self.a, self.b)

    __repr__ = __str__

    # 四則演算定義
    def __add__(self, other):
        if other.__class__ == Fraction:
            x = self.a * other.b + self.b * other.a
            y = self.b * other.b
        elif other.__class__ == int:
            x = self.a - self.b * other
            y = self.b
        else:
            assert 0, "型が違う"
        return Fraction(x, y)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if other.__class__ == Fraction:
            x = self.a * other.b - self.b * other.a
            y = self.b * other.b
        elif other.__class__ == int:
            x = self.a + self.b * other
            y = self.b
        else:
            assert 0, "型が違う"
        return Fraction(x, y)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if other.__class__ == Fraction:
            x = self.a * other.a
            y = self.b * other.b
        elif other.__class__ == int:
            x = self.a * other
            y = self.b
        else:
            assert 0, "型が違う"

        return Fraction(x, y)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        if other == Fraction():
            raise ZeroDivisionError

        H = self / other
        return H.a // H.b

    def __rfloordiv__(self, other):
        if self == Fraction():
            raise ZeroDivisionError

        H = other / self
        return H.a // H.b

    def __truediv__(self, other):
        assert other, "除数が0"

        if other.__class__ == Fraction:
            x = self.a * other.b
            y = self.b * other.a
        elif other.__class__ == int:
            x = self.a
            y = self.b * other
        else:
            assert 0, "型が違う"

        return Fraction(x, y)

    def __rtruediv__(self, other):
        assert self, "除数が0"
        if other.__class__ == Fraction:
            x = other.a * self.b
            y = other.b * self.a
        elif other.__class__ == int:
            x = other * self.b
            y = self.a
        else:
            assert 0, "型が違う"
        return Fraction(x, y)

    def __pow__(self, m):
        alpha, beta = self.a, self.b
        if m < 0:
            alpha, beta = beta, alpha
            m = -m

        return Fraction(pow(alpha, m), pow(beta, m))

    # 丸め
    def __floor__(self):
        return self.a // self.b

    def __ceil__(self):
        return (self.a + self.b - 1) // self.b

    # 真偽値
    def __bool__(self):
        return bool(self.a)

    # 比較
    def __eq__(self, other):
        if other.__class__ == Fraction:
            return self.a * other.b == self.b * other.a
        elif other.__class__ == int:
            return self.a == self.b * other
        else:
            assert 0, "型が違う"

    def __nq__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self <= other and self != other

    def __le__(self, other):
        if other.__class__ == Fraction:
            return self.a * other.b <= self.b * other.a
        elif other.__class__ == int:
            return self.a <= self.b * other
        else:
            assert 0, "型が違う"

    def __gt__(self, other):
        return other <= self and other != self

    def __ge__(self, other):
        return other <= self

    # その他
    def __float__(self):
        return self.a / self.b

    def sign(self):
        s = self.a * self.b
        if s > 0:
            return 1
        elif s == 0:
            return 0
        else:
            return -1

    # 符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Fraction(-self.a, self.b)

    def __abs__(self):
        if self.a > 0:
            return self
        else:
            return -self

    # その他
    def is_unit(self):
        return self.a == 1

    def __hash__(self):
        return hash(10 ** 9 * self.a + self.b)


# ================================================


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    min_list = []
    max_list = []
    for x, y in grid:
        min_list.append(Fraction((y - 1), x))
        max_list.append(Fraction(y, (x - 1)))

    i_list = sorted(range(len(min_list)), key=lambda i: max_list[i])

    current_rmax = Fraction(0, 1)
    count = 0
    for i in i_list:
        if current_rmax <= min_list[i]:
            current_rmax = max_list[i]
            count += 1

    print(count)


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
1 1
2 1
1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
414598724 87552841
252911401 309688555
623249116 421714323
605059493 227199170
410455266 373748111
861647548 916369023
527772558 682124751
356101507 249887028
292258775 110762985
850583108 796044319"""
        output = """10"""
        self.assertIO(input, output)
