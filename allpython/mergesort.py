def mergeSort(arr):
  if len(arr) <= 1:
      return arr
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]
  left_half = mergeSort(left_half)
  right_half = mergeSort(right_half)
  return merge(left_half, right_half)

def merge(left, right):
  merged = []
  i = j = 0
  while i < len(left) and j < len(right):
      if left[i] < right[j]:
          merged.append(left[i])
          i += 1
      else:
          merged.append(right[j])
          j += 1
  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged
arr = [7, 2, 1, 6, 8, 5, 3, 4]
sorted_arr = mergeSort(arr)
print("Sorted array:", sorted_arr)