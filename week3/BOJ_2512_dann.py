import sys

input = sys.stdin.readline

N = int(input())
N_val = list(map(int, input().split()))
M = int(input())

l, r = 0, max(N_val)
mid = 0
while l <= r:
  mid = (l + r) // 2
  sum_of_val = 0
  for val in N_val:
    if val <= mid:  # 요청예산보다 지정값이 작으면 요청예산을 더한다
      sum_of_val += val
    else:  # 요청예산보다 지정값이 크면 지정값을 더한다
      sum_of_val += mid
  if sum_of_val <= M:  # 예산의 합이 최댓값보다 작으면, 예산의 최솟값을 증가시킨다
    l = mid + 1
  else:  # 예산의 합이 최댓값보다 크면, 예산의 최댓값을 감소시킨다
    r = mid - 1
print(r)