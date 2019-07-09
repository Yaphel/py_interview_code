def set_arr(arr):
  arr_len=len(arr)
  left_point,right_point=0,arr_len-1
  while right_point>left_point:
    a=set_arr_rules(arr[left_point],arr[right_point])
    if a is 3:
      arr[left_point],arr[right_point]=arr[right_point],arr[left_point]
      left_point+=1
      right_point-=1
    elif a is 2:
      right_point-=1
    elif a is 1:
      left_point+=1
    elif a is 0:
      right_point-=1
      left_point+=1
  return arr

def set_arr_rules(a,b):
  if a%2 is 1 and b%2 is 0:
    return 0
  elif a%2 is 0 and b%2 is 1:
    return 3
  elif a%2 is 1 and b%2 is 1:
    return 1
  else:
    return 2
  
print(set_arr([1,2,3,4,5,6,7,9]))
