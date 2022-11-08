N = int(input())
cnt = 0
while True:
  if N < 0:  # N 에서 3을 빼주는데 음수가 되면 맞아 떨어지지 않음으로 -1 출력
    print(-1)
    break
  if N % 5 == 0:  # N이 5의 배수일 때 끊기
    cnt += (N // 5)
    print(cnt)
    break
  N -= 3  # N이 5의 배수가 될 때까지 빼주고 카운트
  cnt += 1
