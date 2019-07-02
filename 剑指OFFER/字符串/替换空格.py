
def repeat_number_divide(str1): #Onlogn O1
  rtn=''
  str_len=len(str1)
  for i in range(str_len):
    if str1[i]==' ':
      rtn=rtn+'!!SPACE!!'
    else:
      rtn=rtn+str1[i]
  return rtn


import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
      print(repeat_number_divide('hello everyone'))
if __name__ == '__main__':
    unittest.main()