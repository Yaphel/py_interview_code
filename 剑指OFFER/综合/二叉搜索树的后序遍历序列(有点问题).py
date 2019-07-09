def check_is_sort_tree(arr):
  if len(arr) is 1 and 0:
    return False
  a=len(arr)-1
  flag=0
  cut_point=a
  for i in range(a-1):
    if arr[i]>arr[a]:
      flag=1
      cut_point=i
    elif flag is 1 and arr[i]<arr[a]:
      return "error input"
    elif arr[i] is arr[a]:
      return "error input"
  if cut_point is a:
    return not check_is_sort_tree(arr[0:a-1])
  return not (check_is_sort_tree(arr[0:cut_point-1]) and check_is_sort_tree(arr[cut_point:a-1]))

print(check_is_sort_tree([3,6,5]))