n = int(input())
dict = {}
answer = []

for i in range(n):
  name, work = input().split()
  if work == 'enter':
    dict[name] = i
    # value 값 지정해야하는데 할게 없어서
  else:
    dict.pop(name)

# 사전의 역순 정렬 이므로 dict는 순서는 없는데 정렬은 가능한것 같아요
for key,value in sorted(dict.items(), key = lambda x:x[0],reverse = True):
  print(key)

