import sys
sys.setrecursionlimit(4100000)

from itertools import permutations


def resolve():
    N_vertex, M_edge = [int(x) for x in sys.stdin.readline().split()]
    edge_set = set([
        tuple(int(x) for x in sys.stdin.readline().split())
        for _ in range(M_edge)
    ])
    # print(edge_set)

    count = 0
    for p in permutations(range(1, N_vertex + 1)):
        # print(p)
        if p[0] != 1:
            continue
        is_broken = False
        for i in range(N_vertex - 1):
            if (p[i], p[i + 1]) in edge_set or (p[i + 1], p[i]) in edge_set:
                pass
            else:
                is_broken = True
                break
        if not is_broken:
            count += 1

    print(count)


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
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)
