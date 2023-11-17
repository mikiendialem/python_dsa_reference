def sumofclosest(arr,t):
  n=len(arr)
  res=arr[0]+arr[1]+arr[2]
  for i in range(n-2):
    l=i+1
    r=n-i
    while l<r:
      out=arr[i]+arr[l]+arr[r]
      if out == t:
        return out
      elif out > t:
        r-=1
      else:
        l+=1
      if abs(out-t) < abs(res-t):
        res=out
  return res
arr=[1,2,3,4,5,6,8]
t=10
print(sumofclosest(arr,t))