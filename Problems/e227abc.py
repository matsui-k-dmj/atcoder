# むずすぎわろた
# import sys
# # sys.setrecursionlimit(4200000)


# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # import math

# from collections import defaultdict

# def resolve():
#     S = sys.stdin.readline().split()[0]  # 文字列 一つ
#     K = int(sys.stdin.readline().split()[0])  # int 一つ
#     L = len(S)

#     S = S.lower()

#     dp = [[[defaultdict(int) for _ in range(L+1)] for i in range(L + 1)] for j in range(L+1)]

#     dp[0][0][0][0] = 0

#     for i in range(L):
#         for n_k in range(i + 1):
#             for n_e in range(i + 1 - n_k):
#                 current_n = {"k": 0, "e": 0, "y": 0}
#                 found = {"k": False, "e": False, "y": False}
#                 count_not_in = 0
#                 n_y = i - n_k - n_e
#                 assert(n_y >= 0)
#                 for j, c in enumerate(S):
#                     if c == "k":
#                         if current_n[c] < n_k:
#                             current_n[c] += 1
#                         else:
#                             if not found[c]:
#                                 found[c] = True
#                                 for k, v in dp[i][n_k][n_e].items():
#                                     if k + count_not_in <= K:
#                                         dp[i+1][n_k + 1][n_e][k + count_not_in] += 1
#                             count_not_in += 1
                            

#                     elif c == "e":
#                         if current_n[c] < n_e:
#                             current_n[c] += 1
#                         else:
#                             if not found[c]:
#                                 found[c] = True
#                                 for k, v in dp[i][n_k][n_e].items():
#                                     if k + count_not_in <= K:
#                                         dp[i+1][n_k][n_e + 1][k + count_not_in] += 1
#                             count_not_in += 1
#                     else:
#                         if current_n[c] < n_y:
#                             current_n[c] += 1
#                         else:
#                             if not found[c]:
#                                 found[c] = True
#                                 for k, v in dp[i][n_k][n_e].items():
#                                     if k + count_not_in <= K:
#                                         dp[i+1][n_k][n_e][k + count_not_in] += 1
#                             count_not_in += 1

#                     if found["k"] and found["e"] and found["y"]:
#                         break

#     count = 0
#     for v in dp[L][S.count("k")][S.count("e")].values():
#         count += v

#     print(count)

# if __name__ == "__main__":
#     resolve()

# # AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# # python -m unittest hoge.py
# # pypy3 -m unittest hoge.py

# import sys
# from io import StringIO
# import unittest


# class TestClass(unittest.TestCase):
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)

#     def test_入力例_1(self):
#         input = """KEY
# 1"""
#         output = """3"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """KKEE
# 2"""
#         output = """4"""
#         self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """KKEEYY
# 1000000000"""
#         output = """90"""
#         self.assertIO(input, output)


