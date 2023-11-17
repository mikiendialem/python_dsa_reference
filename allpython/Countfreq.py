def countfreq(arr):
  x=sorted(arr)
  count=1
  for i in range(len(x)):
    if x[i]==x[i+1]:
      count+=1
    else:
      break
  return count
arr=[1,3,6,2,5,7]
print(countfreq(arr))
