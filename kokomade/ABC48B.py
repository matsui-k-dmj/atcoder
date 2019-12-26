import math
def main(a, b, x):
    b_floor = b // x

    if(a % x > 0):
        a_ceil = a // x + 1
    else:
        a_ceil = a // x

    print(b_floor - a_ceil + 1)

if __name__ == "__main__":
    a, b, x = [int(x) for x in input().split()]
    main(a, b, x)

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