import sys
input = sys.stdin.readline
from bisect import bisect_left


n = int(input())
for i in range(n):
  result = 0
  x,y = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  b.sort()
    
  for target in a:
    
    a = bisect_left(b,target)
    result += a
    
  print(result)

# 이진으로 풀어볼려 했으나 ... 추후에 bisect외에 풀린다면 다시 제출 하겠습니다

