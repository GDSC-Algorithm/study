sugar = int(input())
result = 0
while sugar != 0:
    if sugar < 0:
        result = -1
        break

    if (sugar % 5) == 0:
        result += (sugar // 5)
        sugar = 0
    else:
        sugar -= 3
        result += 1

print(result)