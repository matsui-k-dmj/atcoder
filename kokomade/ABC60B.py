import math
def main(a, b, c):
    for i in range(b):
        if (a * i) % b == c:
            print('YES')
            return

    print('NO')

if __name__ == "__main__":
    a, b, c = [int(x) for x in input().split()]
    main(a, b, c)

def test1(capsys):
    inputs = [7, 5, 1]
    out = 'YES'
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test3(capsys):
    inputs = [2, 2, 1]
    out = 'NO'
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test4(capsys):
    inputs = [1, 100, 97]
    out = 'YES'
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test5(capsys):
    inputs = [40, 98, 58]
    out = 'YES'
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'