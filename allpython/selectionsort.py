def selectionSort(arr):
  n = len(arr)
  for i in range(n):
      min_index = i
      for j in range(i + 1, n):
          if arr[j] < arr[min_index]:
              min_index = j
      arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [7, 2, 1, 6, 8, 5, 3, 4]
selectionSort(arr)
print("Sorted array:", arr)