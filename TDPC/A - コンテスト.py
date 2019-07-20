import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    p_list = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(N, p_list))

    def res(i):
        if (i == N):
            return set([0])
        else:
            ret_sets = res(i + 1)
            return set([s + p_list[i] for s in ret_sets]) | ret_sets

    print(len(res(0)))


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

    def test_Sample_Input_1(self):
        input = """3
2 3 5"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
1 1 1 1 1 1 1 1 1 1"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
1"""
        output = """2"""
        self.assertIO(input, output)
