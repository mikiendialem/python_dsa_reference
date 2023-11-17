def reverserstring(arr):
  #we can do it by two pointers
  n=len(arr)
  l=0
  r=n-1
  while l<r:
    arr[l],arr[r] = arr[r],arr[l]
    l +=1
    r-=1
  return arr

arr=['h','e','l','l','o']
print(reverserstring(arr))