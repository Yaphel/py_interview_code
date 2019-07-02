#二分查找,要求是要排好序，Ologn
def divide_find(arr,data):
  arr_len=len(arr)
  start=0
  end=arr_len-1
  middle=(start+end)//2
  if data < arr[start] or data > arr[end]:
    print("data overflow")
    return None
  if data is arr[start]:
    print("found!",start)
    return None  
  if data is arr[middle]:
    print("found!",middle)
    return None
  if data is arr[end]:
    print("found!",end)
    return None
  if data < arr[middle] and data > arr[start]:
    return divide_find(arr[start:middle],data)
  else:
    return divide_find(arr[middle+1:end],data)

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(divide_find([1,2,3,4,5],3))
    print(divide_find([1,2,3,4,5],6))
if __name__ == '__main__':
  unittest.main()