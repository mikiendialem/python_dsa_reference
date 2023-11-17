def maxm(arr):
  maxm=arr[0]
  for elements in arr:
    if elements > maxm:
        maxm=elements
  return maxm

arr=[1,4,6,2,5,7]
print(maxm(arr))