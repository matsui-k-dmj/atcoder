import sys
from io import StringIO
import unittest
import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import re


def resolve():
    s_prime = sys.stdin.readline().split()[0]
    T = sys.stdin.readline().split()[0]
    logger.debug(s_prime)
    logger.debug(T)

    s_len = len(s_prime)
    t_len = len(T)

    r_s_prime = s_prime[::-1]
    r_t = T[::-1]

    answer = "UNRESTORABLE"
    for i_s, s_char in enumerate(r_s_prime):
        if s_len - i_s >= t_len:
            is_match = True
            for i_t, t_char in enumerate(r_t):
                if r_s_prime[i_s + i_t] == '?' or r_s_prime[i_s +
                                                            i_t] == t_char:
                    pass
                else:
                    is_match = False
                    break

            if is_match:
                answer = r_s_prime[:i_s] + r_t + r_s_prime[i_s + len(r_t):]
                answer = answer[::-1]
                pattern = re.compile(r'\?')
                answer = pattern.sub('a', answer)
                break
        else:
            break

    print(answer)


if __name__ == "__main__":
    resolve()


# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる
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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """?
a"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """?
ab"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """??????????
abc"""
        output = """aaaaaaaabc"""
        self.assertIO(input, output)