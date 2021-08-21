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

    max1, max2 = sorted(a_list, reverse=True)[:2]

    for a in a_list:
        if a == max1:
            print(max2)

        else:
            print(max1)


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
        input = """3
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1
1"""
        output = """1
1"""
        self.assertIO(input, output)