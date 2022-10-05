T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    a.sort()
    b.sort()

    # 이분탐색
    for j in range(n):
        start = 0
        end = m - 1
        while start <= end:
            temp = (start + end) // 2 
            if a[j] <= b[temp]:
                end = temp - 1
            else: 
                # a[j]>b[temp]인데 구간 안에 원소가 하나뿐인 경우 
                # 인덱스가 temp인 경우를 포함해서 갯수를 세기 위해 미리 1을 더해줌
                if start == end: 
                    count += 1
                start = temp + 1
        # while문의 결과: b의 크기 중에서 a의 크기보다 작은 수 중 최댓값의 인덱스(최댓값까지의 개수)가 temp로 저장됨
        count += temp # temp이전의 인덱스에서는 모두 a>b이므로 temp를 더해줌

    print(count)

