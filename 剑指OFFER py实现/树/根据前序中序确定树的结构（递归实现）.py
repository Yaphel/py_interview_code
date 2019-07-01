class TNode(object):
    def __init__(self,data,lc = None,rc = None):
        self.data = data
        self.lc = lc
        self.rc = rc

def constructor(before,middle):#寻找树的根节点
  if len(before) is not 0:
    node=TNode(before[0])
    trans=find_number_in_m(before[0],middle)
    node.lc=constructor(before[1:trans+1],middle[0:trans])
    node.rc=constructor(before[trans+1:],middle[trans+1:])
    return node
  else:
    return None

def find_number_in_m(left_number,middle):
  for i in range(len(middle)):
    if left_number is middle[i]:
      return i 
  return None #输入有误

def print_before(node):#再次打印前序遍历，对比输入结果。
  if node:
    print(node.data)
    print_before(node.lc)
    print_before(node.rc)
import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(print_before(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))
if __name__ == '__main__':
  unittest.main()