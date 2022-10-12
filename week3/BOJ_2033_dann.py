N = list(input())


def rounder(integer_n):
  if integer_n > 4:
    return True
  else:
    return False


for i in reversed(range(1, len(N))):
  if rounder(int(N[i])):
    N[i] = '0'
    N[i - 1] = str(int(N[i - 1]) + 1)
  else:
    N[i] = '0'
print(''.join(N))
