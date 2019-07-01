def repeat_number_hash(arr): #On On
  arr_len=len(arr)
  li=[0]*arr_len
  rep=set()
  for i in arr:
    li[arr[i]]+=1
  for i in range(0,arr_len):
    if li[i]>1:
      rep.add(i)
  print (rep)

def repeat_number_sort(arr): #Onlogn O1
  arr.sort()
  arr_len=len(arr)
  rep=set()
  a=-1
  for i in range(1,arr_len):
    if arr[i]==arr[i-1] and a!=arr[i]:
      a=arr[i]
      rep.add(a)
      continue
    elif a==arr[i]:
      continue
    else:
      continue
  print (rep)


import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(repeat_number_hash([0,1,2,3,4,0]))
  def test_02(self): 
    print(repeat_number_hash([1,1,2,3,4,5]))
  def test_03(self): 
    print(repeat_number_hash([2,2,2,3,4,5]))
  def test_04(self): 
    print(repeat_number_hash([3,1,2,3,4,5]))
  def test_05(self): 
    print(repeat_number_hash([4,2,2,3,4,5]))
  def test_06(self): 
    print(repeat_number_sort([0,1,2,3,4,0]))
  def test_07(self): 
    print(repeat_number_sort([1,1,2,3,4,5]))
  def test_08(self): 
    print(repeat_number_sort([2,2,2,3,4,5]))
  def test_09(self): 
    print(repeat_number_sort([3,1,2,3,4,5]))
  def test_10(self): 
    print(repeat_number_sort([4,2,2,3,4,5]))


  
if __name__ == '__main__':
    unittest.main()
