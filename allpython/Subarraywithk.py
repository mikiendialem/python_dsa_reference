def subarraysum(arr,k):
  res=0
  cur=0
  prefix={0:1}
  for i in arr:
    cur += i
    diff=cur-k
    res +=prefix.get(diff,0)
    prefix[cur] = prefix.get(cur,0)+1
  return res
arr=[1,1,1]
k=2
print(subarraysum(arr,k))
      