import sys

# 알고리즘은 맞았으나, sys.stdin.readline을 써야 시간초과가 안되는 문제였음
n,m = map(int,input().split())
dict = {}
count = 0
for i in range(m):
  num = sys.stdin.readline().rstrip()
  dict[num] = i


for key, value in sorted(dict.items(), key = lambda x:x[1]):

  print(key)
  count += 1
  if count == n:
    break

'''
원래제출 코드

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dict = {}
count = 0
for i in range(m):
  num = int(input())
   -> 여기서 문제가 있어서 틀린 것 같은데, rstrip으로 개행제거가 안되서 그런 것 같은데
      궁금한점은 int로 변환하면 개행같은 경우는 자연스레 제거가 되지 않는지가 의문
  dict[num] = i


for key, value in sorted(dict.items(), key = lambda x:x[1]):

  print(key)
  count += 1
  if count == n:
    break

'''