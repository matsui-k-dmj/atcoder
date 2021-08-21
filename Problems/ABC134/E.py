import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    a_list = [[int(x) for x in sys.stdin.readline().split()][0]
              for _ in range(N)]

    logger.debug('{} {}'.format(N, a_list))

    min_list = [10**10]
    max_min = 10**10
    i_max = 0
    for i, a in enumerate(reversed(a_list)):
        if a >= max_min:
            max_min = a
            min_list.append(a)
            i_max = i
        else:
            min_list[i_max] = a
            max_min = max(min_list)

    print(len(min_list))


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
2
1
4
5
3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
0
0
0
0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
0"""
        output = """1"""
        self.assertIO(input, output)