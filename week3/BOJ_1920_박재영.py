def binary_search(list, num):
    start = 0
    end = len(list) - 1
    result = False

    while start <= end:
        half = (start + end) // 2
        if list[half] == num:
            result = True
            break
        elif list[half] < num:
            start = half + 1
        else:
            end = half - 1
    return result

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

a_list.sort()

for i in range(m):
    if binary_search(a_list, b_list[i]) == True:
        print(1)
    else: print(0)
