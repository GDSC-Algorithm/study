t = int(input())


def check(mid, A):
    if mid < A:
        return True
    else:
        return False


for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    count=0
    for i in a:
        start = 0
        end = m - 1
        answer = -1
        while start <= end:
            mid = (start + end) // 2
            if check(b[mid], i):
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        answer+=1
        count+=answer

    print(count)
