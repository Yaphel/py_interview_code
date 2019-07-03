def merge_sort(arr1,arr2):
  arr1_len=len(arr1)
  arr2_len=len(arr2)
  arr3=[]
  i=j=0
  while i<arr1_len and j<arr2_len:
    if arr1[i]<arr2[j]:
      arr3.append(arr1[i])
      i+=1
    elif arr1[i] is arr2[j]:
      arr3.append(arr1[i])
      arr3.append(arr2[j])
      i+=1
      j+=1
    elif arr1[i] > arr2[j]:
      arr3.append(arr2[j])
      j+=1
  if i==arr1_len and j!=arr2_len:
    arr3=arr3+arr2[j:]
  elif i!=arr1_len and j==arr2_len:
    arr3=arr3+arr1[i:]
  return arr3

print(merge_sort([1,2,3,9],[2,3,4,7]))