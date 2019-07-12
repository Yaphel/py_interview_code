def count_array(arr):
  a=0
  max_a=0
  for i in range(len(arr)):
    #此处的异常识别方式有误，不能识别负数。
    #if not str(arr[i]).isdigit():
    #  return "error input"
    a+=arr[i]
    if a<0:
      a=0
    if a>max_a:
      max_a=a
  return max_a

print(count_array([-1,-2,1,2,3,4,-5,-6]))
    
      