def quick_sort(arr):
  if len(arr)>=2:
    left,right=[],[]
    flag=arr[0]
    arr.remove(flag)
    for i in arr:
      if i>flag:
        right.append(i)
      else:
        left.append(i)
    return quick_sort(left)+[flag]+quick_sort(right)
  else:
    return arr

print(quick_sort([1,2,3,4,5,4,3,2]))