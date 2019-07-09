def min_k(arr,k):
  rtn=['0']*k
  if len(arr)<k:
    return "error input"
  for i in range(k):
    rtn[i]=arr[i]
  for i in arr[k:]:
    rtn=set_min(i,rtn)
  return rtn

def set_min(number,rtn):#此处用二分可以在logn内完成操作
  rtn_len=len(rtn)
  if number<rtn[0]:
    rtn=[number]+rtn[0:rtn_len-1]
    return rtn
  elif number>rtn[rtn_len-1]:
    return rtn
  for i in range(rtn_len):
    if number<rtn[i]:
      rtn=rtn[0:i]+[number]+rtn[i:rtn_len-1]
      return rtn
  return rtn

print(min_k([1,2,3,4,5,6,7,8],4))
