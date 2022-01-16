import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from heapq import heappush, heappop

from collections import defaultdict

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, value):
        heappush(self.queue, value)

    def pop(self):
        return heappop(self.queue)

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item):
        return item in self.queue


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    a, N = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    dist = defaultdict(lambda : 10**6)
    queue = PriorityQueue()

    queue.push((0, 1))  # 距離, index
    dist[1] = 0

    L = len(str(N))

    while len(queue):
        dist_current, current_x = queue.pop()
        if dist[current_x] < dist_current:
            continue
        if len(str(current_x)) > L:
            continue
        new_x = current_x * a
        new_dist = dist_current + 1
        if new_dist < dist[new_x] and len(str(new_x)) <= L:
            dist[new_x] = new_dist
            queue.push((dist_current + 1, new_x))
        if current_x >= 10 and current_x % 10 != 0:
            s = str(current_x)
            new_x = int(s[-1] + s[:-1])
            if new_dist < dist[new_x] and len(str(new_x)) <= L:
                dist[new_x] = dist_current + 1
                queue.push((dist_current + 1, new_x))

    print(dist.get(N, -1))



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
        input = """3 72"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 611"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 767090"""
        output = """111"""
        self.assertIO(input, output)

