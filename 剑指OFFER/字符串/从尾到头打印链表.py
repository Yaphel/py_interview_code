class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
      
class Stack(object):
    def __init__(self, top = None):
        self.top = top

    def push(self,data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def isEmpty(self):
        return self.peek() is None

def build_node(arr):
  arr_len=len(arr)
  head_node=Node(arr_len)
  p=head_node
  for i in range(arr_len):
    p.next=Node(arr[i])
    p=p.next
  return head_node

def print_reverse_linklist_stack(node):
  s=Stack()
  node_len=node.data
  node=node.next
  while node is not None:
    s.push(node.data)
    node=node.next
  for i in range(node_len):
    print(s.pop())
  return "over"

def print_reverse_linklist_recursion(node):
  if node is not None:
    print_reverse_linklist_recursion(node.next)
    print(node.data)
    
import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(print_reverse_linklist_stack(build_node([1,2,3])))
  def test_02(self): 
    print(print_reverse_linklist_recursion(build_node([1,2,3]).next))
if __name__ == '__main__':
  unittest.main()

