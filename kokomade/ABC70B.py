
def main(A, B, C, D):
    start = min(A, C)
    end = max(B, D)
    alice_list = [1 if A <= i < B else 0 for i in range(start, end)]
    bob_list = [1 if C <= i < D else 0 for i in range(start, end)]

    print(sum([all(t) for t in zip(alice_list, bob_list)]))
    

if __name__ == "__main__":
    A, B, C, D = [int(x) for x in input().split()]

    main(A, B, C, D)

def test1(capsys):
    inputs = [0, 75, 25, 100]
    out = 50
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test3(capsys):
    inputs = [0, 33, 66, 99]
    out = 0
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test4(capsys):
    inputs = [10, 90, 20, 80]
    out = 60
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'

def test5(capsys):
    inputs = [10, 50, 50, 90]
    out = 0
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == str(out) + '\n'