def seek(start,end,n,limit,array):

  list_ans  = []
  while start <= end:
    
    mid = (start + end)//2

    if mid > 0:
      temp = sum(array[:mid]) + array[mid]*(n-mid)
    else:
      temp = array[mid]*n

    if temp <= limit:
      list_ans.append((temp,mid))
      start = mid + 1
    else:
      end = mid - 1
  
  if not(list_ans):
    return None
    
  return max(list_ans, key = lambda x:(x[0],x[1]))

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
limit = int(input())

if sum(nums) <= limit:
  print(nums[-1])
else:
  result = seek(0,n-1,n,limit,nums)
  if result == None:
    print(limit//n)
  else:
    divide = (limit - result[0])//(n-result[1]-1)
    print(nums[result[1]] + divide)
  

