#要求是不占用额外空间

#可记录重复数字的二叉排序树
class Tnode(object):
  def __init__(self,data):
    self.data=data
    self.count=1
    self.lc=None
    self.rc=None
    self.next=None
    self.prev=None

def constructor(arr):
  arr_len=len(arr)
  root=Tnode(arr[0])
  for i in range(1,arr_len):
    constructor_slave(arr[i],root)
  return root

def constructor_slave(number,node): #此方法有问题
  if number<node.data:
    if node.lc is None:
      node.lc=Tnode(number)
    else:
      node=node.lc  
      constructor_slave(number,node)

  if number>node.data:
    if node.rc is None:
      node.rc=Tnode(number)
    else:
      node=node.rc
      constructor_slave(number,node)

  if number is node.data:
    node.count+=1

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
      
def middle_traversal(troot):
  if troot.lc is None and troot.rc is None:
    return [troot,troot]#只有一个值，左值就是右值
  elif troot.lc is not None and troot.rc is None:
    #有左没有右
    return chain(middle_traversal(troot.lc),[troot,troot])
  elif troot.lc is None and troot.rc is not None:
    #有左没有右
    return chain([troot,troot],middle_traversal(troot.rc))
  else:
    return chain(chain(middle_traversal(troot.lc),[troot,troot]),middle_traversal(troot.rc))

def chain(troot1,troot2):
  troot1[1].next,troot2[0].prev=troot2[0],troot1[1]
  return [troot1[0],troot2[1]]

def link_list_traversal_next(troot):
  if troot is not None:
    print(troot.data,end=' ')
    troot=troot.next
    link_list_traversal_next(troot)

def link_list_traversal_prev(troot):
  if troot is not None:
    print(troot.data,end=' ')
    troot=troot.prev
    link_list_traversal_prev(troot)


import unittest


class MyTest(unittest.TestCase):
  def test_01(self): 
    root=constructor([5,3,7,2,4,6,8])

    #print(root.lc.lc.data)
    print("the biggest number is :",middle_traversal(root)[1].data)
    link_list_traversal_next(middle_traversal(root)[0])
    link_list_traversal_prev(middle_traversal(root)[1])
    #前后都检查一遍
if __name__ == '__main__':
  unittest.main()