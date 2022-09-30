import sys

a, b = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)

sum = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            if nums[i] + nums[j] + nums[k] > b: # 세 개의 숫자를 더한 값이 M보다 클 경우 지나침
                continue
            else: # 문제 조건을 만족하는 경우
                sum = max(sum, nums[i] + nums[j] + nums[k]) # 이전에 계산된 sum과 비교해서 더 큰 값 저장

print(sum)
