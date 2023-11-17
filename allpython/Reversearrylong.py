def reverserarr(arr):
    start=0
    end=len(arr)-1
    while start<end:
      arr[start],arr[end] == arr[end],arr[start]
      start +=1
      end -=1
    return arr
arr=[1,3,6,2,5,7]
print(reverserarr(arr))