def find_someone_2_dimension(arr,rows,columns,num): #On O1
  #错误检测
  if arr[0][0]>num or arr[rows-1][columns-1]<num:
    return 0
  row=0
  column=columns-1
  while row<rows and column>=0:
    if arr[row][column]==num:
      return True
    elif arr[row][column]>num:
      column-=1
    elif arr[row][column]<num:
      row+=1
  return False
  
import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
      print(find_someone_2_dimension(
        [
          [1,2,3,4],
          [2,3,4,5],
          [5,6,7,8],
          [7,8,9,11]
        ],4,4,7))
if __name__ == '__main__':
    unittest.main()