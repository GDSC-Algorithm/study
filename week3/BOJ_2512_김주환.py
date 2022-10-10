n = int(input())
request = list(map(int, input().split()))
total = int(input())


def check(mid):
    global total
    sum = 0
    for i in range(n):
        #원하는 예산보다 편성안이 크면 원하는 예산으로
        if mid > request[i]:
            sum += request[i]
        else:
            sum += mid
    else:
        if sum <= total:
            return True
        else:
            return False


start = 0
end = 100000 #max(request) 가능
answer= 0
while start <= end:
    if sum(request)<=total:
        answer=max(request)
        break
    mid=(start+end)//2
    if check(mid):
        start=mid+1
        answer=mid
    else:
        end=mid-1

print(answer)