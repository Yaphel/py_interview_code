#实现了前序，后序也就简单了。把链表反向即可，不过要给数组reverse一下。
#链表实现树的后序遍历（非递归）

class Node(object):
  def __init__(self,data,next = None):
    self.data = data
    self.before = next
    self.flag = 0 #记录被访问的变量
  def push_before(node):
    self.before = node

class TNode(object):
  def __init__(self,data,lc = None,rc = None):
      self.data = data
      self.lc = lc
      self.rc = rc

#构造树
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

def print_after_recursion(node):#再次打印后序遍历，对比输入结果。
  if node:
    print_after_recursion(node.lc)
    print_after_recursion(node.rc)
    print(node.data)

def print_after_not_recursion(tree):
  s = Node(tree)
  check_link_list(s)
  rtn=[]
  while 1:
    if s is not None:
      rtn.append(s.data.data)
      s=s.before
    else:
      rtn.reverse()
      return rtn

def check_link_list(s):
  while s is not None:
    if s.flag is 0:
      #拆解与装配
      lflag=rflag=0
      if s.data.lc is not None:
        lc=Node(s.data.lc)
        lflag=1
      if s.data.rc is not None:
        rc=Node(s.data.rc)
        rflag=1
      if lflag ==1 and rflag ==1:
        rc.before=lc
        lc.before=s.before
        s.before=rc 
      if lflag ==1 and rflag ==0:
        lc.before=s.before
        s.before=lc      
      if lflag ==0 and rflag ==1:
        rc.before=s.before
        s.before=rc
      s.flag=1
    s=s.before

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print("recursion:",print_after_recursion(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))
    print("not recursion:",print_after_not_recursion(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))
if __name__ == '__main__':
  unittest.main()
