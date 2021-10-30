import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from collections import deque


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    M = int(sys.stdin.readline().split()[0])  # int 一つ

    edge_list = [[] for _ in range(9)]
    for _ in range(M):
        a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
        edge_list[a].append(b)
        edge_list[b].append(a)

    p_position_list = [int(x) - 1 for x in sys.stdin.readline().split()]  # 複数int

    p_list = [-1] * 9
    for j, pj in enumerate(p_position_list):
        p_list[pj] = j

    p_list = tuple(p_list)

    # logger.debug("{}".format([]))

    visited = set()
    correct_p_list = (0, 1, 2, 3, 4, 5, 6, 7, -1)
    i_empty = 0
    for i in range(9):
        if p_list[i] == -1:
            i_empty = i

    dist = -1
    found = False
    queue = deque()
    queue.append((i_empty, p_list, 0, -1))
    while queue:
        i_empty, p_list, dist, i_parent = queue.popleft()
        if p_list in visited:
            continue
        else:
            visited.add(p_list)
        if p_list == correct_p_list:
            found = True
            break

        dist += 1
        for i_next_empty in edge_list[i_empty]:
            if i_next_empty == i_parent:
                continue
            next_p_list = list(p_list)
            next_p_list[i_empty] = next_p_list[i_next_empty]
            next_p_list[i_next_empty] = -1
            queue.append((i_next_empty, tuple(next_p_list), dist, i_empty))

    if found:
        print(dist)
    else:
        print(-1)


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
        input = """5
1 2
1 3
1 9
2 9
3 9
3 9 2 4 5 6 7 8"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2
1 3
1 9
2 9
3 9
1 2 3 4 5 6 7 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12
8 5
9 6
4 5
4 1
2 5
8 9
2 1
3 6
8 7
6 5
7 4
2 3
1 2 3 4 5 6 8 7"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """12
6 5
5 4
4 1
4 7
8 5
2 1
2 5
6 9
3 6
9 8
8 7
3 2
2 3 4 6 1 9 7 8"""
        output = """16"""
        self.assertIO(input, output)
