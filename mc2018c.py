"""dfs, 隣接リスト, ２部グラフ, 彩色
"""
import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
from functools import reduce
from collections import Counter
from collections import defaultdict
# d = defaultdict(list)


def resolve():
    global N, a_list, angelFlags, neighbor_list, is_correct, counts
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    a_list = [int(sys.stdin.readline().split()[0]) - 1 for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    neighbor_list = [[] for _ in range(N)]  # グラフを隣接リストで持てば有向グラフでもdfsできる
    for i, a in enumerate(a_list):
        neighbor_list[i].append(a)
        neighbor_list[a].append(i)
    angelFlags = [0 for _ in range(N)]  # 1, -1, 0, False == 0なのでめっちゃ注意

    is_correct = 1
    counts = defaultdict(int)
    for i in range(N):
        if angelFlags[i] == 0:
            angelFlags[i] = 1
            counts[i] += 1
            dfs(i, i)
            if not is_correct:
                print(-1)
                return

    print(sum([math.ceil(c / 2) for c in counts.values()]))


def dfs(i, i_origin):
    global N, a_list, angelFlags, neighbor_list, is_correct, counts
    for i_next in neighbor_list[i]:
        if angelFlags[i_next] == 0:
            angelFlags[i_next] = -angelFlags[i]
            counts[i_origin] += 1
            dfs(i_next, i_origin)
        else:  # ループしてて終了
            if angelFlags[i_next] == (-angelFlags[i]):
                continue
            else:
                is_correct = False
                continue


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

    def test_入力例_1(self):
        input = """4
2
3
4
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2
3
1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
2
3
4
1
6
5"""
        output = """3"""
        self.assertIO(input, output)