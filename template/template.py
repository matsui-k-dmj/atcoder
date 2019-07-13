from .. import utils

def main(N, A):
    print('{} {}'.format(N, A))


if __name__ == "__main__":
    N, A = [int(x) for x in input().split()]

    main(N, A)

def test1(capsys):
    inputs = [15, 1]
    out = '{} {}'.format(15, 1)
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == '{}\n'.format(out)

def test2(capsys):
    inputs = [2, 3]
    out = '{} {}'.format(2, 3)    
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == '{}\n'.format(out)