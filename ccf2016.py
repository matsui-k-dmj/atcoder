import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    K = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    a_ord = ord("a")
    z_index = ord("z") - a_ord

    s_ord = [ord(s) - a_ord for s in S]
    for i, s in enumerate(s_ord):
        if z_index + 1 - s > K or s == 0:
            continue
        else:
            s_ord[i] = 0
            K -= z_index - s + 1

    mod = ord("z") - a_ord + 1
    if K > 0:
        K = K % mod
        s_ord[-1] = (s_ord[-1] + K) % mod

    print("".join([chr(x + a_ord) for x in s_ord]))


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
        input = """xyz
4"""
        output = """aya"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """a
25"""
        output = """z"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """codefestival
100"""
        output = """aaaafeaaivap"""
        self.assertIO(input, output)
