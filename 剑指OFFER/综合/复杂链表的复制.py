class Node(object):
  def __init__(self,data,number):
    self.data=data
    self.next=None
    self.angle=None
    self.number=number

#三种方法：
# 1.通常的复制，但是在寻找节点的过程，需要再次遍历链表。On^2
# 2.哈希，把节点，节点配对，节点位置放到哈希里面，这样搜索效率为O1，避免了遍历链表的On。
# 3.换种方式。
#  1 2 3  -> 11 22 33 -> 123 123

def constructor(data_arr,angle_arr):
  head=Node(data_arr[0],0)
  p=head
  for i in range(1,len(data_arr)):
    p.next=Node(data_arr[i],i)
    p=p.next
  for i in range(len(angle_arr)):
    p1,p2=head,head
    for j in range(i):
      p1=p1.next
    if angle_arr[i] is not None:
      for k in range(angle_arr[i]-1):
        p2=p2.next
      p1.angle=p2
    else:
      p1.angle=None
  return head

def normal_copy(head):
  p_for_copy_data=head.next
  new_link_head=Node(head.data)
  p_for_new_link_head_data=new_link_head
  while p_for_copy_data is not None:
    p_for_new_link_head_data.next=Node(p_for_copy_data.data,p_for_copy_data.number)
    p_for_new_link_head_data=p_for_new_link_head_data.next
    p_for_copy_data=p_for_copy_data.next
  #copy data ok

  p_for_copy_angle=head.next
  p_for_new_link_head_angle=new_link_head  
  while p_for_copy_angle is not None:
    p_for_new_link_head_angle.angle=find_node(new_link_head,p_for_copy_angle.number)
    p_for_new_link_head_angle=p_for_copy_angle.next
    p_for_copy_angle=p_for_copy_angle.next
  #copy angle ok

  return new_link_head

def find_node(head,n):
  for i in range(n):
    if head.next is None:
      return "error"
    else:
      head=head.next
  return head

def quick_copy(head):
  p=head

  copy_data(head)
  copy_angle(head)

  print("copy ok")
  #copy ok
  rtn=divide(head)
   #divide ok
  return rtn

def copy_data(head):
  p=head
  while 1:
    if p is None:
      return head
    newNode=Node(p.data,p.number)
    newNode.next=p.next
    p.next=newNode
    p=p.next.next
def copy_angle(head):
  p=head
  while 1:
    if p.angle is not None:
      p.next.angle=p.angle.next
    p=p.next.next
    if p is None:
      return head
def divide(head):
  flag=0
  if head is None:
    return None
  new_head=head.next
  head=head.next.next
  while 1:
    if head is None:
      return new_head
    print(new_head.data)
    if flag is 1:
      new_head.next=head.next
      new_head=new_head.next
      head=head.next
      flag=0
    elif flag is 0:
      head=head.next
      flag=1

def print_link(head):
  while 1:
    if head is None:
      print("end")
      return 0
    if head.angle is not None:
      print(head.data,head.angle.data,end=' ')
      #print(head.data,end=' ')
    else:
      print(head.data,"None",end=' ')
      #print(head.data,end=' ')
    head=head.next

#test constructor
print_link(constructor([1,2,3,4,5],[3,5,None,2,None]))
#test quick_copy
print_link(quick_copy(constructor([1,2,3,4,5],[3,5,None,2,None])))