def heapSort(arr):
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
      heapify(arr, n, i)
  for i in range(n - 1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i]
      heapify(arr, i, 0)
def heapify(arr, n, i):
  largest = i  # Initialize largest as the root
  left = 2 * i + 1
  right = 2 * i + 2
  if left < n and arr[left] > arr[largest]:
      largest = left
  if right < n and arr[right] > arr[largest]:
      largest = right
  if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)
arr = [7, 2, 1, 6, 8, 5, 3, 4]
heapSort(arr)
print("Sorted array:", arr)