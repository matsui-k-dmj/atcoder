import sys
sys.setrecursionlimit(4100000)


def resolve():
    N, A = [int(x) for x in sys.stdin.readline().split()]

    print('{} {}'.format(N, A))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる