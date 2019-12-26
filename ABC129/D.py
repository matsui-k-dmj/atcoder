import numpy as np

def main(H, W, s_list):
    row_count = np.zeros((H, W))
    for i_row in range(H):
        i_col = 0
        j_col = 0
        s = s_list[i_row]
        while(i_col < W):
            char = s[i_col]
            j_col = i_col
            
            if char == '.':
                while(True):
                    j_col += 1
                    if j_col == W:
                        break
                    c = s[j_col]
                    if c == '#':
                        break

                row_count[i_row, i_col:j_col] = j_col - i_col
            i_col = j_col + 1


    col_count = np.zeros((H, W))
    for i_col in range(W):
        i_row = 0
        j_row = 0
        s_col = [s[i_col] for s in s_list]
        while(i_row < H):
            char = s_col[i_row]
            j_row = i_row
            if char == '.':
                while(True):
                    j_row += 1
                    if j_row == H:
                        break
                    c = s_col[j_row]
                    if c == '#':
                        break
                
                col_count[i_row:j_row, i_col] = j_row - i_row
            i_row = j_row + 1
    print(int(np.max(row_count + col_count)) - 1)



if __name__ == "__main__":
    H, W = [int(x) for x in input().split()]
    s_list = []
    for _ in range(H):
        s_list.append(input())

    main(H, W, s_list)
