def twosum(arr,k):
  n=len(arr)
  cur=0
  prefix={0:0}
  for i in range(n):
    cur += arr[i]
    diff=cur-k
    if diff in prefix:
      return [prefix[diff],i]
    prefix[cur]=i+1
  return [-1 -1]
arr=[3,2,4]
k=6
print(twosum(arr,k))