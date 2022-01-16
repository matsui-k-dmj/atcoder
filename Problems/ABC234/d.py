"""
heap
"""
import sys
# sys.setrecursionlimit(4200000)

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


import heapq

class Heapq:
    def __init__(self, _list=None):
        if _list is not None:
            self.heap = _list
            heapq.heapify(self.heap)
        else:
            self.heap = []

    def pop(self):
        return heapq.heappop(self.heap)

    def push(self, x):
        heapq.heappush(self.heap, x)

def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    p_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    heap = Heapq(p_list[:K])

    print(heap.heap[0])

    for i in range(K+1, N+1):
        p = p_list[i-1]
        if p > heap.heap[0]:
            heap.pop()
            heap.push(p)
        print(heap.heap[0])




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
        input = """3 2
1 2 3"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11 5
3 7 2 5 11 6 1 9 8 10 4"""
        output = """2
3
3
5
6
7
7"""
        self.assertIO(input, output)


