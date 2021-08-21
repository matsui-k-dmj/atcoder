
def main(s_list):
    if len(s_list) == 1 and s_list[0] == '#':
        print('Yes')
        return

    for i_row, s in enumerate(s_list):
        for j_col, char in enumerate(s):
            if char == '#':
                neighbor_list = []
                try:
                    neighbor_list.append(s_list[i_row-1][j_col])
                except:
                    pass
                try:
                    neighbor_list.append(s_list[i_row+1][j_col])
                except:
                    pass
                try:
                    neighbor_list.append(s_list[i_row][j_col-1])
                except:
                    pass
                try:
                    neighbor_list.append(s_list[i_row][j_col+1])
                except:
                    pass
                
                if neighbor_list.count('#') == 0:
                    print('No')
                    return

    print('Yes')

if __name__ == "__main__":
    H, W = [int(x) for x in input().split()]
    s_list = []
    for i in range(H):
        s_list.append(input())

    main(s_list)

def test1(capsys):
    inputs = ['.#.', '###', '.#.']
    out = 'Yes'
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == out + '\n'

def test2(capsys):
    inputs = ['#.#.#', '.#.#.', '#.#.#', '.#.#.', '#.#.#']
    out = 'No'
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == out + '\n'

def test3(capsys):
    inputs = ['...#####...', '.##.....##.', '#..##.##..#', '#..##.##..#', '#.........#', '#...###...#', '.#########.', '.#.#.#.#.#.', '##.#.#.#.##', '..##.#.##..', '.##..#..##.']
    out = 'Yes'
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == out + '\n'

def test4(capsys):
    inputs = ['#']
    out = 'Yes'
    main(inputs)
    captured = capsys.readouterr()    
    assert captured.out == out + '\n'