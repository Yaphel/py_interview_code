def heap_constructor(arr):
  #解决树的序号和数组开头的问题。
  arr_len=len(arr)-1
  i=arr_len//2
  while i>0:
    arr=heap_constructor_slave(arr,i)
    if i*2 <= arr_len//2:
      arr=heap_constructor_slave(arr,i*2)
    if i*2+1 <= arr_len//2:
      arr=heap_constructor_slave(arr,i*2+1)
    i-=1
  return arr

     
def heap_constructor_slave(arr,i):
  arr_len=len(arr)-1
  if i*2+1<=arr_len:
    if arr[i*2+1]<arr[i*2]:
      if arr[i*2+1]<arr[i]:
        arr=exchange(arr,i*2+1,i)
    else:
      if arr[i*2]<arr[i]:
        arr=exchange(arr,i*2,i)
  else:
    if arr[i*2]<arr[i]:
      arr=exchange(arr,i*2,i)
  return arr


def exchange(arr,a,b):
  arr[a],arr[b]=arr[b],arr[a]
  return arr
  
#解决树的序号和数组开头的问题。
print(heap_constructor([-1,7,6,5,4,3,2,1]))