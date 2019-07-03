#插入排序，从小到大
def insert_sort(arr,n):
  arr_len=len(arr)
  flag=arr_len
  for i in range(arr_len):
    if n<arr[i]:#控制顺序
      flag=i
      break
  arr=back_and_push(arr,flag,n)
  return arr
    
def back_and_push(arr,point,data):#point为第一个比data大的数字，如果没有，就返回串长
  arr_len=len(arr)
  arr.append(arr[arr_len-1])
  i=arr_len-1
  while i>point:
    arr[i]=arr[i-1]
    i-=1
  arr[point]=data
  return arr
    

def insert_constructor(arr):
  rtn=[arr[0]]
  arr_len=len(arr)
  for i in range(1,arr_len):
    rtn=insert_sort(rtn,arr[i])
  return rtn

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(insert_constructor([5,4,3,2,1])) 
  def test_02(self): 
    print(insert_constructor([5,4,3,2,1,1,2,3,4,5])) 
if __name__ == '__main__':
  unittest.main()