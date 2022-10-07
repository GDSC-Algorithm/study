import sys
input = sys.stdin.readline

# INPUT
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))
    # 정렬
    a=sorted(a)
    b=sorted(b)
    
    # result : 결과, num : b의 인덱스
    result,num = 0, 0
    for i in range(x):
        
      while True:
        if num == y: 
          result += num
          break
          
        elif a[i] <= b[num]:
          result +=num
          break
          
        else:
          num += 1
    print(result)

