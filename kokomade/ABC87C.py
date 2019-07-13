import math
import numpy as np
def main(N, a1, a2):
    a1_cum = np.cumsum(a1)
    a2_cum = np.cumsum(a2)

    print(max([a1_cum[i] + a2[i] + (a2_cum[-1] - a2_cum[i]) for i in range(N)]))


if __name__ == "__main__":
    N = int(input())
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    
    main(N, a1, a2)

def test1(capsys):
    inputs = [4, 8, 2]
    out = 3
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test3(capsys):
    inputs = [0, 5, 1]
    out = 6
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test4(capsys):
    inputs = [9, 9, 2]
    out = 0
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test5(capsys):
    inputs = [1, 1000000000000000000, 3]
    out = 333333333333333333
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'