T = int(input())

for i in range(T):
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  B = sorted(list(map(int, input().split())))
  cnt = 0
  for a in A:
    l, r = 0, M - 1
    result = 0
    while l <= r:
      mid = (l + r) // 2
      if a <= B[mid]:  # a가 지정값보다 작으면 범위의 최댓값을 왼쪽으로 당긴다
        r = mid - 1
      else:  # a가 지정값보다 크면 범위의 최솟값을 오른쪽으로 당긴다
        l = mid + 1
        result = l  # a보다 작은값들 중 최댓값이 정답이 된다
    cnt += result
  print(cnt)
