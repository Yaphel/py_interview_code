#我把问题分成两种思路：
#从左向右搜索和从右向左搜索。
#从左向右搜索的必要条件有三个：拆分，乘积，运算。（将字符串拆成数个子串，独立计算每个子串的可能性数目，再依次乘积）
#从整的方法上来看，这种方式具有可行性且没有无效计算。那么就从此着手了。

def divide(arr):#拆分环节
  #拆分有两个决策思路：1.遇到大于2的拆到下一个。2.遇到大于2大头的跳过。
  rtn_list=[]
  now_list=[]
  for i in arr:
    if i>2:
      if len(now_list) is 0:
        continue#直接跳过
      else:
        rtn_list.append(calculate(now_list))
        now_list=[]
    else:
      now_list.append(i)
  if len(now_list) is not 0:
    rtn_list.append(calculate(now_list))
  return rtn_list

def calculate(arr):
  #计算涉及到三种类型的问题：
  # 1122  11228  11226  结果分别为4,4,5
  #考虑好以上三种问题即可
  if arr[len(arr)-1]>6:
    return len(arr)
  else:
    return len(arr)+1

def multply(arr):
  rtn=1
  for i in arr:
    rtn*=i
  return rtn

print(multply(divide([1,1,2,8,8,1,2])))