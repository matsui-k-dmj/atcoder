import string

def bubble_sort(num_list):
    if len(num_list) == 1:
        return num_list
    elif len(num_list) == 2:
        print("? {} {}".format(num_list[0], num_list[1]), flush=True)
        ans = input()
        if (ans == '<'):
            return num_list
        else:
            return list(reversed(num_list))

    else:
        i_sep = len(num_list) // 2
        former_list = bubble_sort(num_list[:i_sep])
        later_list = bubble_sort(num_list[i_sep:])

        result_list = []
        i_former = 0
        i_later = 0
        while(True):
            if len(former_list) == i_former:
                result_list.extend(later_list[i_later:])
                return result_list
            elif len(later_list) == i_later:
                result_list.extend(former_list[i_former:])
                return result_list
            else:
                former_num = former_list[i_former]
                later_num = later_list[i_later]
                print("? {} {}".format(former_num, later_num), flush=True)
                ans = input()
                if (ans == '<'):
                    result_list.append(former_num)
                    i_former += 1
                else:
                    result_list.append(later_num)
                    i_later += 1


if __name__ == "__main__":
    N, Q = [int(x) for x in input().split()]
    upper_chars = string.ascii_uppercase    
    sorted_list = bubble_sort(list(upper_chars[:N]))
    print("! {}".format(''.join(sorted_list)), flush=True)