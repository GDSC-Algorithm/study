n = int(input())
mul=[1,10,100,1000,10000,100000,1000000,100000000]

if len(str(n)) == 1:
    print(n)
else:
    for i in range(1,len(str(n))):
        if int(str(n)[-i]) >= 5:
            n += (10 - int(str(n)[-i]))*mul[i-1]
        else:
            n -= (int(str(n)[-i]))*mul[i-1]
    print(n)