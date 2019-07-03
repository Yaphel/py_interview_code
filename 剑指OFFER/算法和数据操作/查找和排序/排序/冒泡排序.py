def bubble_sort(arr):
  arr_len=len(arr)
  for i in range(arr_len):
    for j in range(arr_len-1):
      if arr[j]>arr[j+1]:
        t=arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=t
  return arr

print(bubble_sort([1,2,3,3,2,1]))
