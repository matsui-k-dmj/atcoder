import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

import re

def resolve():
    S = sys.stdin.readline().split()[0]

    logger.debug(S)
    p = re.compile(r'\?')
    q_index_list = [m.span()[0] for m in p.finditer(S)]
    logger.debug(q_index_list)

    new_s_list = list(S)
    for i in q_index_list:
        new_s_list[i] = '0'

    zero_s = int(''.join(new_s_list))

    r = (5 - (zero_s % 13)) % 13

    old_count_dict = dict(zip(range(13), [0]*13))
    old_count_dict[r] = 1

    for i in q_index_list:
        order = len(S) - i - 1

        order_mod = order % 13

        new_count_dict = dict(zip(range(13), [0]*13))

        for j in range(10):
            x = (order_mod * j) % 13
            for k in range(13):
                r = (k - x) % 13
                new_count_dict[r] += old_count_dict[k]
        
        old_count_dict = new_count_dict

    print(old_count_dict[5] % (10**9 + 7))

if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

