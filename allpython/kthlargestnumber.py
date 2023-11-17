def kthlargestnumber(arr,k):
  n=len(arr)
  if n<k:
    return -1
  if n==k:
    return arr[k-1]
  arr.sort()
  return arr[n-k]
  
arr=[-1,2,0]
k=3
print(kthlargestnumber(arr,k))