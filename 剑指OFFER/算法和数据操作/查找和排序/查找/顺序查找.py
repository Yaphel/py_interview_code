#最简单的查找，On
def normal_find(arr,data):
  arr_len=len(arr)
  for i in range(arr_len):
    if arr[i]==data:
      return "found: "+str(data)+" in "+str(i)
  return "not found "+ str(data)

  

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(normal_find([1,2,3,4,5],3))
    print(normal_find([1,2,3,4,5],6))
if __name__ == '__main__':
  unittest.main()