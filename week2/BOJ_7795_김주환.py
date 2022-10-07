n = int(input())

for _ in range(n):
    result = 0
    (a, b) = tuple(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)

    for aa in range(a):
        aCount = 0
        for bb in range(b):
            if A[aa] > B[bb]:
                aCount += 1
                result += len(B) - bb
                break
        if aCount == 0:
            break
    print(result)