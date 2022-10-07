n = int(input())
num_list = list(map(int, input().split()))
budget = int(input())

# (각 지방의 예산 상한값 < 총 예산) 이므로
# 총 예산(target)까지의 정수가 저장된 리스트에서 상한값이 될만한 정수를 찾아보도록 하자
limit_list = [i+1 for i in range(max(num_list))] 
start = 0
end = max(num_list) - 1

while start <= end:
    half = (start + end) // 2
    
    sum = 0
    for i in num_list:
        sum += min(i, limit_list[half]) # 예산 요청과 상한값 후보(index=half인 값) 중 작은 값 더하기
    
    if sum == budget:
        limit = limit_list[half]
        break
    elif sum > budget:
        end = half - 1
    else:
        limit = limit_list[half]
        start = half + 1
    

print(limit)