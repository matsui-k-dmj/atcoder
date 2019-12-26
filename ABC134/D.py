import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


# @profile
def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(N, a_list))

    box_list = [0 for _ in range(N)]

    for i in reversed(range(N)):
        suma = sum(box_list[i:N:i+1])

        r = suma % 2
        if r != a_list[i]:
            box_list[i] = 1

    s = sum(box_list)
    print(s)

    if s > 0:
        print(' '.join(
            [str(i + 1) for i in range(len(box_list)) if box_list[i]]))


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
1 0 0"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)