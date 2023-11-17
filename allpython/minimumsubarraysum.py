def minimalsubarray(arr, k):
  n=len(arr)
  min_length=float('inf')
  for start in range(n):
    sum=0
    for end in range(start,n):
      sum +=arr[end]
      if sum >=k:
        min_length=min(min_length,end-start+1)
        break
  if min_length==float('inf'):
    return -1
  else:
    return min_length

print(minimalsubarray([1, 4, 41, 7, 0, 19], 51))
    
