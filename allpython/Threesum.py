def threesum(arr):
  #arr[i]+arr[j]+arr[k]=0
  n=len(arr)
  arr.sort()
  res=[]
  for i in range(n):
    j= i+1
    k=n-1
    while j<k:
      if arr[i]+arr[j]+arr[k]<0:
        j+=1
      elif arr[i]+arr[j]+arr[k]>0:
        k-=1
      else:
        res.append([arr[i],arr[j],arr[k]])
        while j<k and arr[j]==arr[j+1]:
          j+=1
        while j<k and arr[k]==arr[k-1]:
          k-=1
        j+=1
        k-=1
  return res

arr = [-1,0,1,2,-1,-4]
print(threesum(arr))