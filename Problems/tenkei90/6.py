"""
006 - Smallest Subsequence（★5） https://atcoder.jp/contests/typical90/tasks/typical90_f
辞書順

前からレンジを狭めつつ最小/最大とか取る場合は、後ろから前処理すればいい。
"""
import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

# from collections import defaultdict


def resolve():
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    S = sys.stdin.readline().split()[0]  # 文字列 一つ

    L = len(S)
    c = [[L] * 26 for _ in range(len(S) + 1)]
    base = ord('a')
    for i in range(len(S))[::-1]:
        for j_char in range(26):
            char = ord(S[i]) - base
            if char == j_char:
                c[i][j_char] = i
            else:
                c[i][j_char] = c[i+1][j_char]


    n_selected = 0
    ret_s = ''
    last_char_index = -1
    for i in range(len(S)):
        if i <= last_char_index:
            continue
        for char, last_char_index in enumerate(c[i]):
            if L - last_char_index + n_selected >= K:
                n_selected += 1
                ret_s += chr(char + base)
                break

        if n_selected == K:
            break

    print(ret_s)

    





if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py
