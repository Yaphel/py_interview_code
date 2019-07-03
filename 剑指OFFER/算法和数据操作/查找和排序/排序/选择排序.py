def selection_sort(arr,n):
  arr_len=len(arr)
  temp=n
  for i in range(n,arr_len):
    if arr[temp]>arr[i]:
      temp=i
  arr=exchange(arr,n,temp)
  return arr

def exchange(arr,a,b):
  arr[a],arr[b]=arr[b],arr[a]
  return arr

print(selection_sort([1,2,3,4,5,9,8,7,6],5))