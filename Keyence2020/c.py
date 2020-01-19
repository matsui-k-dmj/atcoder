import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, K, S = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    if S >= 2:
        S = str(S)

        ans = [S] * K
        if K < N:
            ans += ['1']

        ans += ['0'] * (N - K - 1 if N - K - 1 > 0 else 0)
    else:
        S = str(S)

        ans = [S] * K
        if K < N:
            ans += ['10']

        ans += ['0'] * (N - K - 1 if N - K - 1 > 0 else 0)

    print(' '.join(ans))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる
