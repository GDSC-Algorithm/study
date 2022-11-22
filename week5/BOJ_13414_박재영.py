# 자꾸 시간초과되는데........ 시간초과 안되는 방법을 모르겠어서.... 우선 이 코드 제출해요...
# 구글링해보니까 학번 = input().rstrip()을 하던데 이거 때문일까..?
# .rstrip()은 오른쪽 공백 제거라는데 왜 하는건지 모르겠습니다..ㅠ.

import sys

input = sys.stdin.readline
max, n = map(int, input().split())
st_list = {}

for i in range(n):
    st = input()
    st_list[st] = i
# print(st_list)

st_list = sorted(st_list.items(), key = lambda x: x[1]) # value 기준으로 오름차순 정렬

count = 0
for key, value in st_list:
    if count == max:
        break
    print(key)
    count += 1
