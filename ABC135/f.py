import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N, D = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(N, D))



if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

