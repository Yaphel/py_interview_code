#这道题的前提是数组中是确认存在这样的数字的
def find_number(arr):
  if len(arr) is 0:
    return "error input"
  a,b=arr[0],1
  for i in arr[1:]:
    if i is a:
      b+=1
    else:
      b-=1
    if b is -1:
      b=1
      a=i
  return a

print(find_number([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,4,6,4,3,5,6,3,4,5,4,3,2,1]))
