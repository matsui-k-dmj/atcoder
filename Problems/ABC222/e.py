"""
木の最短経路はdfsでO(n)
通った辺は簡単にわかる。

部分和問題は O(N * sum)で簡単
典型的な DP (動的計画法) のパターンを整理 Part 1 ～ ナップサック DP 編 ～ - Qiita https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E3%81%8A%E3%82%8F%E3%82%8A%E3%81%AB


"""
import sys

# sys.setrecursionlimit(4100000)

import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) - 1 for x in sys.stdin.readline().split()]  # 複数int

    count_dict = dict()
    edge_list = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
        edge_list[a].append(b)
        edge_list[b].append(a)
        count_dict[
            (min(a, b), max(a, b))
        ] = 0  # こうしなくても 辺の添え字iもedge listに入れといて、それでインデクスすればいい

    def dfs(i, goal, i_parent):
        # 木の最短経路で通った辺をカウントするdfs
        if i == goal:
            return True

        for next in edge_list[i]:
            if next != i_parent:
                if dfs(next, goal, i):
                    count_dict[(min(i, next), max(i, next))] += 1
                    return True

    for i in range(M - 1):
        dfs(a_list[i], a_list[i + 1], -1)

    # logger.debug("{}".format([count_dict]))

    count_list = list(count_dict.values())
    s = sum(count_list)

    if (K + s) % 2 == 1 or (K + s) < 0:
        print(0)
        return

    dp = [0] * (s + 1)  # 和は最高sだから
    dp[0] = 1
    MOD = 998244353
    for i in range(len(count_list)):
        for k in range(count_list[i], s + 1)[::-1]:  # 後ろから回すと配列再利用できる
            dp[k] += dp[k - count_list[i]]
            dp[k] %= MOD

    if (K + s) // 2 > s:
        print(0)
    else:
        print(dp[(K + s) // 2])

    # 結局 K は マイナスになるけど、K+s がマイナスになる時は不可能だから先に返せるので、
    # 配列は0始まりで良くなる。


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
        input = """4 5 0
2 3 2 1 4
1 2
2 3
3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 10 10000
1 2 1 2 1 2 2 1 1 2
1 2
1 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 2 -1
1 10
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """126"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 8 -1
1 4 1 4 2 1 3 5
1 2
4 1
3 1
1 5"""
        output = """2"""
        self.assertIO(input, output)
