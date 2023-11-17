def subarraysumsdivisiblebyk(arr,k):
  n=len(arr)
  count=0
  for start in range(n):
    sum=0
    for end in range(start,n):
      sum+=arr[end]
      if sum%k==0:
        count+=1
  return count

arr=[4,5,0,-2,-3,1]
k=5
print(subarraysumsdivisiblebyk(arr,k))