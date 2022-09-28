N, M = map(int, input().split())
cards = list(map(int, input().split()))
length = len(cards)

if N == length:
  max = 0
  for i in range(0, length - 2):  # 첫번쨰 인자의 인덱스는 cards베열의 마지막에서 두번쨰여야 나머지 두 숫자를 더할 수 있으므로 -2번째 인덱스까지 여유를 남겨둠
    for j in range(i + 1, length - 1):  # 위와 동일
      for k in range(j + 1, length):
        sum = cards[i] + cards[j] + cards[k]  # 모든 경우의 숫자를 더한 값
        if M >= sum >= max:  # sum이 주어진 최댓값 이하이고, 이전의 숫자보다 큰 상황을 만족하면 =>
          max = sum  # max에 할당
  print(max)
else:
  print("invalid operation")
