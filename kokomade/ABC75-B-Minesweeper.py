
def main(s_list):
    res_list = []
    for i_row, s in enumerate(s_list):
        res_char_list = []
        for j_col, char in enumerate(s):
            if char == '#':
                res_char_list.append('#')
            else:
                res_char_list.append(str(''.join(
                    [rows[max(j_col-1, 0): j_col+2] for rows in s_list[max(i_row-1, 0):i_row+2]]).count('#')))
        res_list.append(''.join(res_char_list))

    print('\n'.join(res_list))


if __name__ == "__main__":
    H, W = [int(x) for x in input().split()]
    s_list = []
    for i in range(H):
        s_list.append(input())

    main(s_list)

def test1(capsys):
    inputs = ['.....',
        '.#.#.',
        '.....']
    out = ['11211',
        '1#2#1',
        '11211']
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == '\n'.join(out)+'\n'

def test2(capsys):
    inputs = ['#####',
                '#####',
                '#####']
    out = ['#####',
                '#####',
                '#####']
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == '\n'.join(out)+'\n'

def test3(capsys):
    inputs = ['#####.', '#.#.##', '####.#', '.#..#.', '#.##..', '#.#...']
    out = ['#####3', '#8#7##', '####5#', '4#65#2', '#5##21', '#4#310']
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == '\n'.join(out)+'\n'