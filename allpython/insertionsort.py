def insertionSort(arr):
  n = len(arr)
  for i in range(1, n):
      key = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > key:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key
arr = [7, 2, 1, 6, 8, 5, 3, 4]
insertionSort(arr)
print("Sorted array:", arr)