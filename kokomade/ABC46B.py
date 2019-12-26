
def main(N, K):
    print(K * (K-1)**(N-1))

if __name__ == "__main__":
    N, K = [int(x) for x in input().split()]

    main(N, K)

def test1(capsys):
    inputs = [2, 2]
    out = 2
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test3(capsys):
    inputs = [1, 10]
    out = 10
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test4(capsys):
    inputs = [10, 8]
    out = 322828856
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test5(capsys):
    inputs = [1, 2]
    out = 2
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'
