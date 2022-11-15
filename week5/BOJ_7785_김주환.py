import sys
input = sys.stdin.readline
n = int(input())
company={}
for _ in range(n):
    name,status = tuple(input().split())
    company[name] = status
company=dict(sorted(company.items(), key= lambda x:x[0],reverse=True))

for i in company.keys():
    if company[i] == 'enter':
        print(i)
