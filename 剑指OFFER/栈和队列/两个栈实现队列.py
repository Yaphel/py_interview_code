class Node(object):
  def __init__(self,data,next = None):
    self.data = data
    self.next = next

class Stack(object):
  def __init__(self, top = None):
    self.top = top

  def push(self,data):
    self.top = Node(data, self.top)

  def push_arr(self,arr):
    arr_len=len(arr)
    for i in range(arr_len):
      self.push(arr[i])
    return self

  def pop(self):
    if self.top is None:
      return None
    data = self.top.data
    self.top = self.top.next
    return data

  def pop_all(self):
    arr=[]
    a=self.pop()
    while a:
      arr.append(a)
      a=self.pop()
    return arr

  def isEmpty(self):
    return self.peek() is None


class Quene(object):
  def __init__(self,s1,s2):
    #s1是master栈
    #s2是slave栈
    self.s1=s1
    self.s2=s2
  def pop(self):
    self.s2.push_arr(self.s1.pop_all())
    print("Quene pop value : " ,self.s2.pop())
    s=self.s2
    self.s2=self.s1
    self.s1=s
  def push(self,data):
    self.s1.push(data)

import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    q=Quene(Stack().push_arr([1,2]),Stack())
    q.pop()
    q.push(3)
    q.pop()
    q.pop()
if __name__ == '__main__':
  unittest.main()


