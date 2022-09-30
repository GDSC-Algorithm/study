n,m = map(int,input().split())
arr = list(map(int,input().split()))
compare = []

for a in range(n-2) :
    for b in range(a+1,n-1) :
        for c in range(b+1,n) :
            result = arr[a]+arr[b]+arr[c]
            if result <= m :
               compare.append(result)
print(max(compare))