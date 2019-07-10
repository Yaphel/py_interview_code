#只需要按某种规则将数字排序即可。
#排序的规则就是比较mn和nm大小。

def concat_number(m,n):
  mp=get_number_place(m)
  np=get_number_place(n)
  for i in range(m):
    mn=m*10
  for i in range(n):
    nm=n*10
  nm=nm+m
  mn=mn+n
  if nm>mn:
    return "change"
  else:
    return "not change"
def get_number_place(num):
  rtn=0
  while num is not 0:
    rtn+=1
    num=num//10
  return rtn
  
#后面再加个排序就可以了。