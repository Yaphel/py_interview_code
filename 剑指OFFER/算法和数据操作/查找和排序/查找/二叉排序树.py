#可记录重复数字的二叉排序树
class Tnode(object):
  def __init__(self,data):
    self.data=data
    self.count=1
    self.lc=None
    self.rc=None

def constructor(arr):
  arr_len=len(arr)
  root=Tnode(arr[0])
  for i in range(1,arr_len):
    constructor_slave(arr[i],root)
  return root

def constructor_slave(number,node):
  if number<node.data:
    if node.lc is None:
      node.lc=Tnode(number)
      return None
    else:
      node=node.lc  

  if number>node.data:
    if node.rc is None:
      node.rc=Tnode(number)
      return None
    else:
      node=node.rc

  if number is node.data:
    node.count+=1
    return None

def find(root,data):
  while 1:
    if data is root.data:
      return "found "+ str(root.count)
    if data < root.data:
      if root.lc is not None:
        root = root.lc
      else:
        return "not found "+str(data)
    if data > root.data:
      if root.rc is not None:
        root = root.rc
      else:
        return "not found "+str(data)
      


import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    root=constructor([1,2,3,4,5,1,1,1,1,1,1])
    print(find(root,1))
  def test_02(self): 
    root=constructor([1,2,3,4,5,1,1,1,1,1,1])
    print(find(root,7))
if __name__ == '__main__':
  unittest.main()