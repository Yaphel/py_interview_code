#有5张牌，判断是不是顺子，其中大小王为癞子牌。

#A-K为 1-13

#大小王为0
#检查癞子
def check_lai(arr):
  lai=0
  for i in arr:
    if i is 0:
      lai+=1
  return lai


def judge(arr):
  arr.sort()
  arr=list(set(arr))
  if len(arr) is not 5:
    return False
  for i in arr:
    if i is not 0:
      start=i
      break
  if arr[-1]-start is 4-check_lai(arr):
    return True
  else:
    return False

print(judge([1,0,3,3,5]))