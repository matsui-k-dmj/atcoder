# import sys
# # sys.setrecursionlimit(4200000)


# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # sにiが入ってるか
# def include(s, i):
#     return (s >> i) & 1

# def size(s):
#     return bin(s).count("1")

# MOD = 998244353

# def resolve():
#     # S = sys.stdin.readline().split()[0]  # 文字列 一つ
#     N = int(sys.stdin.readline().split()[0])  # int 一つ
#     M = int(sys.stdin.readline().split()[0])  # int 一つ

#     c_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
#     _sum = 0
#     for s in range(1, 1 << M):
#         count = 0
#         inc_zero = False
#         for i in range(M):
#             if include(s, i):
#                 count += 1
#                 if c_list[i] == 0:
#                     inc_zero = True
#         if inc_zero:
#             r = pow(10 - count, N, MOD)
#         else:
#             r = (9 - count) * pow(10 - count, N-1, MOD)
        
#         _sum += (-1)**(count) * r
#         _sum = _sum % MOD

#     _all = 9 * pow(10, N-1, MOD)

#     print((_all - _sum) % MOD)

        


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
#         input = """104
# 2
# 0 1"""
#         output = """520"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """999
# 4
# 1 2 3 4"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# 5
# 0 2 4 6 8"""
#         output = """397365274"""
#         self.assertIO(input, output)

