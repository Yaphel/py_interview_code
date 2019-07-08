import math
def cut_rope(n):
  rtn=[-1,1,2,3]
  for i in range(4,n+1):
    max_arr=build_max_arr(i,rtn)
    rtn.append(max(max_arr))
  return rtn

def build_max_arr(n,arr):
  rtn=[]
  arr_len=len(arr)
  for i in range(1,math.floor(n/2)+1):
    rtn.append(arr[n-i]*arr[i])
  return rtn

print(max(cut_rope(8)))