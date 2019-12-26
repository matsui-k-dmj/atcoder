import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from copy import copy

def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    p_list = [int(x) for x in sys.stdin.readline().split()]

    is_broken = False
    old = p_list[0]
    for p in p_list[1:]:
        if old > p:
            is_broken = True
            break
        old = p

    if not is_broken:
        print("YES")
        return

    for i in range(N):
        for j in range(N):
            if i >= j:
                continue
            p_list_alt = copy(p_list)
            p_list_alt[i], p_list_alt[j] = p_list[j], p_list[i]

            is_broken = False
            old = p_list_alt[0]
            for p in p_list_alt[1:]:
                if old > p:
                    is_broken = True
                    break
                old = p

            if not is_broken:
                print("YES")
                return

    print("NO")

            
            

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
5 2 3 4 1"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
2 4 3 5 1"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6 7"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 2"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """2
2 1"""
        output = """YES"""
        self.assertIO(input, output)





if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

