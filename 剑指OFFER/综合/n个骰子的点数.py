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


#循环解法
def get_n_dice_2(n,s):
  dice1=[0,1,1,1,1,1,1]
  for i in range(2,n+1):
    dice2=[0]*(1+6*i)
    #求dice2
    for j in range(i,1+6*i):
      dice2[j]=get_dice_number(dice1,j)
      #print(i,j,dice2[j],end='')
      #print()
    #进位1
    dice1=dice2
  return [dice1[s],(6**n)]

def get_dice_number(d1,j):
  rtn=0
  for i in range(1,7):
    if j-i >6:
      continue
    if j-i >= 0:
      rtn+=d1[j-i]
    else:
      break
  return rtn
  

print([get_n_dice(3,6),6**3])
print(get_n_dice_2(3,6))



  
