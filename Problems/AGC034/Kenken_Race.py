def count_raw_char(s, char):
    max_len = 0
    current_len = 0
    for c in s:
        if c == char:
            current_len += 1
        else:
            if max_len < current_len:
                max_len = current_len
            current_len = 0

    return max_len

def main(N, A, B, C, D, S):
    if C < D:
        raw_sharp_A = count_raw_char(S[A+1: C], '#')
        raw_sharp_B = count_raw_char(S[B+1: D], '#')
        
        if raw_sharp_A >= 2 or raw_sharp_B >= 2:
            print('No')
            return
        else:
            print('Yes')
            return
    else:
        raw_sharp = count_raw_char(S[A+1: C], '#')
        if raw_sharp >= 2:
            print('No')
            return

        raw_space = count_raw_char(S[B-1: D+2], '.')
        if raw_space >= 3:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    N, A, B, C, D = [int(x) for x in input().split()]
    S = input()

    main(N, A, B, C, D, S)

def test1(capsys):
    main(7, 1, 3, 6, 7, '.#..#..')
    captured = capsys.readouterr()    
    assert captured.out == 'Yes\n'

def test2(capsys):
    main(7, 1, 3, 7, 6, '.#..#..')
    captured = capsys.readouterr()    
    assert captured.out == 'No\n'

def test3(capsys):
    inputs = [15, 1, 3, 15, 13, '...#.#...#.#...']
    out = "Yes"
    main(*inputs)
    captured = capsys.readouterr()    
    assert captured.out == '{}\n'.format(out)