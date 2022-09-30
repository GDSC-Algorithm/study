# 카드 뽑기/ 모든 카드 탐색
def seek(nums, n, m):
  a = 0
  for i in range(0,n-2):
    for j in range(i+1,n-1):
      for k in range(j+1,n):
        if nums[i] +nums[j]+ nums[k] <= m:
            a = max(a,nums[i] +nums[j]+ nums[k])
  return a
        
n,m = map(int,input().split())
numbers  = sorted(list(map(int,input().split())),reverse =True)
print(seek(numbers,n,m))
