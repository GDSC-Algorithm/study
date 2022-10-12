n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
exist = list(map(int, input().split()))


def check(mid, find):
    if mid <= find:
        return True
    else:
        return False


for i in range(m):
    answer = 2147483649 #2^31 보다 큰값으로 맞춰야함
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if check(arr[mid], exist[i]):
            answer = arr[mid]
            start = mid + 1
        else:
            end = mid - 1

    if answer == exist[i]:
        print(1)
    else:
        print(0)

# 여기서부터는 결정함수 없는 버전
for i in range(m):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == exist[i]:
            print(1)
            break
        elif arr[mid] < exist[i]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0)
