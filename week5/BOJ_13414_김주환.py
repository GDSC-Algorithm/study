import sys
input = sys.stdin.readline
k,l = map(int,input().split())
order = {}
for i in range(l):
    student_id = input().rstrip()
    order[student_id] = i

order = sorted(order.items(), key=lambda x:x[1])
cnt = 0
for i in order:
    if cnt == k:
        break
    print(i[0])
    cnt+=1