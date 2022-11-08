n = int(input())
answer = 0
while True:

  if n%5 == 0:
    answer += n//5
    break

  else:
    n -= 3
    answer += 1

  if n < 0:
    answer = -1
    break

print(answer)
  
  # 5를 많이 이용해야 최소로 가능해짐
  # 그래서 5로 나누고 안떨어지면 3을 빼보면서 5로 나누어지는지 확인
  # 만약 3을 계속 뺏는데 나누어지지 않아서 음수가 되면 return -1