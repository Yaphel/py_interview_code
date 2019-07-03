class Node(object):
  def __init__(self, data, next = None):
    self.data=data
    self.next=next
#除法取余法实现hash，拉链法实现解决冲突。
def hash(number,arr):
  arr_len=len(arr)
  hash_list=[0]*number
  for i in range(arr_len):
    count=arr[i] % number
    if hash_list[count] is 0:
      hash_list[count]=Node(arr[i])
    else:
      node=hash_list[count]
      while node.next is not None:
        node=node.next
      node.next=Node(arr[i])
  return hash_list
  
def find(hash_list,data):
  number=len(hash_list)
  count=data % number
  node=hash_list[count]
  while node is not None and node is not 0:
    if node.data is data:
      return "found "+ str(data)
    node=node.next
  return "not found!" + str(data)

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    hash_list=hash(10,[1,2,3,4,5,6,7,8,9,11,2,3,4,5,6,7,8,11,22,33,44,55,66])
    #hash_list=hash(10,[4,4,4,44,33,66])
    print(find(hash_list,44))
    print(find(hash_list,1))
    print(find(hash_list,33))
    print(find(hash_list,66))
    print(find(hash_list,4))
  def test_02(self): 
    #hash_list=hash(10,[1,2,3,4,5,6,7,8,9,11,2,3,4,5,6,7,8,11,22,33,44,55,66])
    hash_list=hash(10,[4,4,4,44,33,66])
    print(find(hash_list,44))
    print(find(hash_list,1))
    print(find(hash_list,33))
    print(find(hash_list,66))
    print(find(hash_list,4))
if __name__ == '__main__':
  unittest.main()
