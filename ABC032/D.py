"""
01ナップサック
"""

import sys
sys.setrecursionlimit(4100000)

import logging

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# メモ化再帰 (やらないほうがいい)
from functools import lru_cache

def resolve():
    N, W = [int(x) for x in sys.stdin.readline().split()]
    v_list = []
    w_list = []
    for _ in range(N):
        v, w = [int(x) for x in sys.stdin.readline().split()]
        v_list.append(v)
        w_list.append(w)

    logger.debug('{} {}'.format(N, W))
    logger.debug(v_list)
    logger.debug(w_list)

    if N <= 30:
        logger.debug('low N')
        @lru_cache(maxsize=None)
        def rec(i, w_rec):
            if i == N:
                return 0
            else:
                if w_rec - w_list[i] >= 0:
                    return max(rec(i+1, w_rec - w_list[i]) + v_list[i], rec(i+1, w_rec))
                else:
                    return rec(i+1, w_rec)

        print(rec(0, W))

    elif max(w_list) <= 1000:
        logger.debug('low w')
        sum_w = sum(w_list)
        lim_w = min(sum_w, W)
        dp = [0]*(lim_w+1)
        for i in range(N):
            for w in range(lim_w+1)[::-1]:
                if w - w_list[i] >= 0:
                    dp[w] = max(dp[w-w_list[i]]+v_list[i], dp[w])
        print(max(dp))

    else:
        logger.debug('low v')
        sum_v = sum(v_list)
        dp = [float('inf')]*(sum_v+1)
        dp[0] = 0
        for i in range(N):
            for v in range(sum_v+1)[::-1]:
                if v - v_list[i] >= 0:
                    dp[v] = min(dp[v-v_list[i]]+w_list[i], dp[v])

        for v, w in zip(range(sum_v+1)[::-1], dp[::-1]):
            # logger.debug("{}, {}".format(v, w))
            if w <= W:
                print(v)
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
        """
        low N
        """
        input = """3 10
15 9
10 6
6 4"""
        output = """16"""
        self.assertIO(input, output)
#     def test_入力例2(self):
#         """
#         low n, どっちも大きい
#         """
#         input = """30 499887702
# 128990795 137274936
# 575374246 989051853
# 471048785 85168425
# 640066776 856699603
# 819841327 611065509
# 704171581 22345022
# 536108301 678298936
# 119980848 616908153
# 117241527 28801762
# 325850062 478675378
# 623319578 706900574
# 998395208 738510039
# 475707585 135746508
# 863910036 599020871686
# 340559411 738084611686
# 122579234 545330131686
# 696368935 867975891686
# 665665204 592749599
# 958833732 401229830
# 371084424 523386474
# 463433600 5310725
# 210508742 907821957
# 685281136 565237085
# 619500108 730556272
# 88215377 310581512
# 558193168 136966252
# 475268130 132739489
# 303022740 12425915
# 122379996 137199296
# 304092766 23505143"""
#         output = """3673016420"""
#         self.assertIO(input, output)
    def test_入力例3(self):
        """
        low w
        """
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
        """
        low v
        """
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

    def test_入力例5(self):
        input = """1 1
1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例6(self):
        """
        low v
        """
        input = """10 1
1 1
1 1
1 1
1 1
1 1
2 1
1 1
1 1
1 1
1 2"""
        output = """2"""
        self.assertIO(input, output)
