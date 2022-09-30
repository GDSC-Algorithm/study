import sys
count = ''
for i in range(int(sys.stdin.readline())):
  N, M = map(int, sys.stdin.readline().split())
  A = [i for i in list(map(int, sys.stdin.readline().split()))]
  B = sorted(i for i in list(map(int, sys.stdin.readline().split())))
  a_bigger_than_b = 0
  for a in A:
    for b in B:
      # a의 요소가 b보다 클 때는 카운팅
      if a > b:
        a_bigger_than_b += 1
        continue
      # break가 없다면 카운팅을 하지만 않고 배열을 계속 탐색하기에 조건을 만족했을 때 해당 요소 탐색을 끝내고 다음 요소로 넘어가서 카운팅
      break
  count += str(a_bigger_than_b) + '\n'
print(count)