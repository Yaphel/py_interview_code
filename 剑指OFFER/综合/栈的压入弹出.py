#书上的方法是效率On的方法。构造模拟栈模拟。
#我想到的方法是检测前面的数字是否小于后面的数字，如果符合这种序列就可以直接判负，效率On^2
def stack_push_and_pop(push,pop):
  arr=[]
  i=j=0
  if len(push) is 0 or len(pop) is 0:
    return "bad input"
  while i<len(push):
    arr.append(push[i])
    if arr[len(arr)-1] is pop[j]:
      arr.remove(arr[len(arr)-1])
      i+=1
      j+=1
    else:
      i+=1
  if j is i:
    return "check ok"
  else:
    return "sorry sir"
    
print(stack_push_and_pop([1,2,3,4,5,6],[1,2,3,4,6,5]))
