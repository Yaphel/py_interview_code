def repeat_number_divide(arr,n): #Onlogn O1
  arr_len=len(arr)
  start=1
  end=n
  middle=(end+start)//2
  while 1:
    count=0
    for i in range(0,arr_len):
      if arr[i]<=middle and arr[i]>=start:
        count+=1
    if count>(middle-start+1):
      end=middle
      middle=(end+start)//2
    else:
      start=middle+1
      middle=(end+start)//2
    if start==end:
      return start

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(repeat_number_divide([1,2,3,4,5,4],5))
  def test_02(self): 
    print(repeat_number_divide([1,2,3,2,5,4,2],5))
  def test_03(self): 
    print(repeat_number_divide([1,2,3,4,5,4,2],6))
  def test_04(self): 
    print(repeat_number_divide([1,2,3,4,4,4,2],4))
  def test_05(self): 
    print(repeat_number_divide([1,2,3,4,5,4,5,2,4,1,2,2,3],5))

      
if __name__ == '__main__':
    unittest.main()