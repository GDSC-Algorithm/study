# 반올림 함수
def roundx(n,count,start):

  foward = int(n[:count] + '0' * (count * (-1)))
  back = n[count]

  if int(back) < 5:
    return str(foward)
  else:
    return str(foward +start)

# 인풋값
n = input()
count = -1
start  = 10

#순차적으로 10,100,1000 ''' 비교
while int(n) > start:
  n = roundx(n,count,start)
  count -= 1
  start *= 10

print(n)
