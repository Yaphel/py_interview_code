class Node(object):
  def __init__(self,data):
    self.data=data
    self.next=None

def set_Node_arr(n):
  rtn=[]
  head=Node(0)
  rtn.append(head)
  for i in range(1,n):
    node=Node(i)
    head.next=node
    head=node
    if i is 1:
      rtn.append(head)
  return rtn

def delete_node(node):
  if node.next :
    node.data=node.next.data
    node.next=node.next.next
  return node

def print_node(node):
  while node.next is not None:
    print(node.data," ")
    node=node.next
  
rtn=set_Node_arr(10)
drtn=delete_node(rtn[1])
print_node(drtn)