"""
E - Traveling Salesman among Aerial Cities https://atcoder.jp/contests/abc180/tasks/abc180_e

最後に行ったノードを管理する必要もある
dp[s][i] で管理する

from_i と to_i で ループするので、2**N * N**2になる。17だと 3.5 * 10**7 くらいでギリギリ通る。
"""

import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

# sにiを追加
def add(s, i):
    return s | (1 << i)

# sからiを除外
def remove(s, i):
    return s & ~(1 << i)

# sにiが入ってるか
def include(s, i):
    return (s >> i) & 1

def size(s):
    return bin(s).count("1")


def resolve():
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    def cost(from_i, to_i):
        a, b, c = grid[from_i]
        p, q, r = grid[to_i]
        return abs(p - a) + abs(q - b) + max(0, r - c)


    dp = [[float('inf')] * N  for _ in range((1 << N))]


    dp[add(0, 0)][0] = 0

    # 空集合以外でループ
    for s in range(1, 1 << N):
        for from_i in range(N):
            # s に含まれてるものでループ
            if not include(s, from_i):
                continue
            for to_i in range(N):
                # 直前の場所には戻らない
                if from_i == to_i:
                    continue
                # 通ったことあるノードにも戻れる。(include(s, to_i) のチェックは必要ない
                next_s = add(s, to_i)
                dp[next_s][to_i] = min(dp[next_s][to_i], dp[s][from_i] + cost(from_i, to_i))


    m = float('inf')
    for i in range(N):
        m = min(m, dp[(1 << N) - 1][i] + cost(i, 0))

    print(m)

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
        input = """2
0 0 0
1 2 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
0 0 0
1 1 1
-1 -1 -1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584"""
        output = """6519344"""
        self.assertIO(input, output)


