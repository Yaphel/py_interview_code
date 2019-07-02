#对于中序非递归，就不能按照之前的方法了。
#所以就用最老套的方法：按照规则遍历树

class TNode(object):
  def __init__(self,data,lc = None,rc = None, parent = None):
      self.data = data
      self.lc = lc
      self.rc = rc
      self.parent = parent
      self.flag = 0

#构造树
def constructor(before,middle,parent = None):#寻找树的根节点
  if len(before) is not 0:
    node=TNode(before[0])
    node.parent=parent
    trans=find_number_in_m(before[0],middle)
    node.lc=constructor(before[1:trans+1],middle[0:trans],node)
    node.rc=constructor(before[trans+1:],middle[trans+1:],node)
    return node
  else:
    return None

def find_number_in_m(left_number,middle):
  for i in range(len(middle)):
    if left_number is middle[i]:
      return i 
  return None #输入有误

def print_middle_recursion(node):#再次打印前序遍历，对比输入结果。
  if node:
    print_middle_recursion(node.lc)
    print(node.data)
    print_middle_recursion(node.rc)

def print_middle_not_recursion(node):
  while 1:
    if node is not None:
      if node.lc is not None and node.lc.flag is 0:
        node = node.lc
      else:
        if node.flag is 0:
          print(node.data)
          node.flag = 1
        if node.rc is not None and node.rc.flag is 0:
          node=node.rc
        else: 
          node=node.parent
    else:
      return None

  

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print("recursion:",print_middle_recursion(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))
    print("not recursion:",print_middle_not_recursion(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))

if __name__ == '__main__':
  unittest.main()