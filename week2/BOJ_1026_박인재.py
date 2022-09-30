N = int(input())
# 큰 숫자순으로 곱해서 더하면 제일 큰 수가 나온다 => 반대로 말하면 큰숫자순, 작은숫자순으로 짝을 지어 더하면 최솟값이 나온다
A = sorted(list(map(int, input().split())))[::-1]
B = sorted(list(map(int, input().split())))

S = 0
for i in range(N):
  S += A[i] * B[i]

print(S)