"""dfs, 隣接リスト, ２部グラフ, 彩色
"""
import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from collections import defaultdict
# d = defaultdict(list)


def resolve():
    global N, neighbor_list, color_list, count_dict
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    neighbor_list = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = sys.stdin.readline().split()
        a = int(a) - 1
        b = int(b) - 1
        neighbor_list[a].append(b)
        neighbor_list[b].append(a)

    logger.debug('{}'.format([]))

    color_list = [None for _ in range(N)]

    count_dict = defaultdict(int)

    dfs(0, 0)

    # こういうのはiteratorで実装するべきやな
    q0_list = list(range(3, N + 1, 3))
    q1_list = list(range(1, N + 1, 3))
    q2_list = list(range(2, N + 1, 3))
    ret_list = [0 for _ in range(N)]
    if count_dict[0] > N // 3 and count_dict[1] > N // 3:
        i_q0 = i_q1 = i_q2 = 0
        for i, c in enumerate(color_list):
            if c == 0:
                if i_q1 < len(q1_list):
                    ret_list[i] = q1_list[i_q1]
                    i_q1 += 1
                else:
                    ret_list[i] = q0_list[i_q0]
                    i_q0 += 1
            else:
                if i_q2 < len(q2_list):
                    ret_list[i] = q2_list[i_q2]
                    i_q2 += 1
                else:
                    ret_list[i] = q0_list[i_q0]
                    i_q0 += 1
        print(' '.join([str(c) for c in ret_list]))
        return

    if count_dict[0] <= N // 3:
        i_q0 = i_q1 = i_q2 = 0
        for i, c in enumerate(color_list):
            if c == 0:
                ret_list[i] = q0_list[i_q0]
                i_q0 += 1

        for i, c in enumerate(color_list):
            if c == 1:
                if i_q0 < len(q0_list):
                    ret_list[i] = q0_list[i_q0]
                    i_q0 += 1
                elif i_q1 < len(q1_list):
                    ret_list[i] = q1_list[i_q1]
                    i_q1 += 1
                else:
                    ret_list[i] = q2_list[i_q2]
                    i_q2 += 1
        print(' '.join([str(c) for c in ret_list]))
        return

    if count_dict[1] <= N // 3:
        i_q0 = i_q1 = i_q2 = 0
        for i, c in enumerate(color_list):
            if c == 1:
                ret_list[i] = q0_list[i_q0]
                i_q0 += 1

        for i, c in enumerate(color_list):
            if c == 0:
                if i_q0 < len(q0_list):
                    ret_list[i] = q0_list[i_q0]
                    i_q0 += 1
                elif i_q1 < len(q1_list):
                    ret_list[i] = q1_list[i_q1]
                    i_q1 += 1
                else:
                    ret_list[i] = q2_list[i_q2]
                    i_q2 += 1
        print(' '.join([str(c) for c in ret_list]))
        return


def dfs(i, color):
    global N, neighbor_list, color_list, count_dict
    color_list[i] = color
    count_dict[color] += 1
    for i_next in neighbor_list[i]:
        if color_list[i_next] is None:  # visited確認
            dfs(i_next, not color)


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
        input = """5
1 2
1 3
3 4
3 5"""
        output = """1 2 5 4 3"""
        self.assertIO(input, output)
