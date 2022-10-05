def round_func(list):
    tmp = -1
    while -tmp < len(list):
        if list[tmp] < 5 :
            list[tmp] = 0
        else:
            if 1-tmp > len(list): # -(tmp-1) = 1-tmp
                list.insert(0, 1)
            else:
                list[tmp-1] += 1
                list[tmp] = 0
        tmp -= 1
    return list
        
n = input()
n_list = list(map(int, [i for i in n]))
nums = list(map(str, round_func(n_list)))

print(int("".join(nums)))