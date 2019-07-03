#[3,4,5,1,2]=>[1,2,3,4,5]
#
def rotate_smallest_digit(arr,start,end):
  if arr[start] < arr[end]:
    return 0
  if arr[start] is arr[end]:
    for i in range(start,end):
      if arr[i]<arr[start]:
        return i
  if end - start is 1:
    return end
  else:
    middle= (end + start) //2
    if arr[end] < arr[middle]:
      return rotate_smallest_digit(arr,middle,end)
    else:
      return rotate_smallest_digit(arr,start,middle)

def rotate_array(arr,pos):
  return arr[pos:]+arr[0:pos]
import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    #arr=[3,4,5,1,2]
    #arr=[1,2,3,4,5]
    arr=[1,0,1,1,1]
    print(rotate_array(arr,rotate_smallest_digit(arr,0,4)))
if __name__ == '__main__':
  unittest.main()
