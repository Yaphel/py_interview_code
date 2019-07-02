#斐波那契还有额外的应用，如：青蛙跳台阶，放置矩形。
#这告诉我们面试的时候也要留意思维的转换。

#不好的方法：从上往下算 F10-F9-F8
#此方法效率低
def fibonacci_recursion(n):
  if n>=2:
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
  if n==1:
    return 1
  if n==0:
    return 0


#好的方法：从下往上算 F1-F2-F3
def fibonacci_count(n):
  fn2=0
  fn1=1
  rtn=1
  for i in range(2,n):
    fn2=fn1
    fn1=rtn
    rtn=fn1+fn2
  return rtn

#装饰器实现


import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(fibonacci_count(10),fibonacci_recursion(10))
if __name__ == '__main__':
  unittest.main()
