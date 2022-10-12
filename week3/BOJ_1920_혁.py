import sys
input = sys.stdin.readline

# 이진탐색 구현 반복문이용
def seek(start,end,target,array):

  while start <= end:

    mid = (start + end) // 2

    if array[mid] == target:
      return True

    elif array[mid] > target:
      end = mid -1

    else:
      start = mid +1

  return False


n = int(input())
a = sorted(list(map(int,input().split())))
m = int(input())
b = list(map(int,input().split()))

for i in b:
  answer = seek(0,n-1,i,a)
  if answer:
    print(1)
  else:
    print(0)


    