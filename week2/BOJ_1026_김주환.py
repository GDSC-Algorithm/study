n= int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sortA = sorted(a)
sortB = sorted(b,reverse=True)
S=0
for i in range(n):
    S+= sortA[i]*sortB[i]

print(S)
