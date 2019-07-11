#基于循环求解。
#构造一种数据结构用来保存n个骰子时候的点数情况。

#递归解法
#dp问题，a[i][j]=a[i-1][j-k](k=1,2,3,4,5,6)
def get_n_dice(n,s):
  if s<n:
    return 0
  if s is n:
    return 1
  if n is 1:
    if s>6:
      return 0
    return 1
  for i in range(n-1):
    rtn=get_n_dice(n-1,s-1)+get_n_dice(n-1,s-2)+get_n_dice(n-1,s-3)+get_n_dice(n-1,s-4)+get_n_dice(n-1,s-5)+get_n_dice(n-1,s-6)
  return rtn

print(get_n_dice(3,6))

#循环解法
def get_n_dice_2(n,s):
  start=[1,1,1,1,1,1]
  
