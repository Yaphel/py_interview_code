#链表实现树的前序遍历（非递归）

class Node(object):
  def __init__(self,data,next = None):
    self.data = data
    self.next = next
    self.flag = 0 #记录被访问的变量
  def push(node):
    self.next = node

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

def print_before_recursion(node):#再次打印前序遍历，对比输入结果。
  if node:
    print(node.data)
    print_before_recursion(node.lc)
    print_before_recursion(node.rc)

def print_before_not_recursion(tree):
  s = Node(tree)
  check_link_list(s)

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
        lc.next=rc
        rc.next=s.next
        s.next=lc      
      if lflag ==1 and rflag ==0:
        lc.next=s.next
        s.next=lc      
      if lflag ==0 and rflag ==1:
        rc.next=s.next
        s.next=rc
      s.flag=1
      print(s.data.data)
    s=s.next

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print("recursion:",print_before_recursion(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))
    print("not recursion:",print_before_not_recursion(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])))
if __name__ == '__main__':
  unittest.main()
