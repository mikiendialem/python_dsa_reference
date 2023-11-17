def partition(arr, low, high):
  i = low - 1
  pivot = arr[high]
  for j in range(low, high):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1
def quickSort(arr, low, high):
  if low < high:
      pivot = partition(arr, low, high)
      quickSort(arr, low, pivot - 1)
      quickSort(arr, pivot + 1, high)
arr = [7, 2, 1, 6, 8, 5, 3, 4]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:", arr)