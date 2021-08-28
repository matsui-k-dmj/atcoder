"""
ナップサック問題
D - ナップサック問題 https://atcoder.jp/contests/abc032/tasks/abc032_d
"""
import sys

# sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from functools import lru_cache


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    v_list = [x[0] for x in grid]
    w_list = [x[1] for x in grid]

    logger.debug("{}".format([]))

    if N == 30:

        @lru_cache(maxsize=None)
        def dp(w, i):
            vi, wi = grid[i]
            if i == N - 1:
                if w < wi:
                    return 0
                else:
                    return vi

            if w < wi:
                return dp(w, i + 1)

            return max(vi + dp(w - wi, i + 1), dp(w, i + 1))

        print(dp(W, 0))

    elif max(w_list) <= 1000:
        dp = [0] * (W + 1)
        for i in range(N):
            for w in reversed(range(W + 1)):  # 逆からじゃないと小さいwが先に更新されてしまう。
                vi, wi = v_list[i], w_list[i]
                if w >= wi:
                    dp[w] = max(dp[w - wi] + vi, dp[w])

        print(max(dp))

    else:
        V = sum(v_list)
        INF = W + 1
        dp = [INF] * (V + 1)
        dp[0] = 0
        for i in range(N):
            for v in reversed(range(V + 1)):  # 逆からじゃないと小さいwが先に更新されてしまう。
                vi, wi = v_list[i], w_list[i]
                if v < vi:
                    dp[v] = min(wi, dp[v])
                else:
                    dp[v] = min(dp[v - vi] + wi, dp[v])

        for v in range(V + 1):
            if dp[v] > W:
                print(v - 1)
                break


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

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

    def test_入力例1(self):
        input = """3 10
15 9
10 6
6 4"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """30 499887702
128990795 137274936
575374246 989051853
471048785 85168425
640066776 856699603
819841327 611065509
704171581 22345022
536108301 678298936
119980848 616908153
117241527 28801762
325850062 478675378
623319578 706900574
998395208 738510039
475707585 135746508
863910036 599020879
340559411 738084616
122579234 545330137
696368935 86797589
665665204 592749599
958833732 401229830
371084424 523386474
463433600 5310725
210508742 907821957
685281136 565237085
619500108 730556272
88215377 310581512
558193168 136966252
475268130 132739489
303022740 12425915
122379996 137199296
304092766 23505143"""
        output = """3673016420"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 2921
981421680 325
515936168 845
17309336 371
788067075 112
104855562 96
494541604 960
32007355 161
772339969 581
55112800 248
98577050 22"""
        output = """3657162058"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10 936447862
854 810169801
691 957981784
294 687140254
333 932608409
832 42367415
642 727293784
139 870916042
101 685539955
853 243593312
369 977358410"""
        output = """1686"""
        self.assertIO(input, output)
