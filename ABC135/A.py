import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    A, B = [int(x) for x in sys.stdin.readline().split()]

    if A == B:
        print(0)
    else:
        if (A - B) % 2 == 0:
            if A > B:
                print(int((A-B) / 2) + B)
            else:
                print(int((B-A) / 2) + A)
        else:
            print("IMPOSSIBLE")



if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

