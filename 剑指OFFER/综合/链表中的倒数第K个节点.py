class Node(object):
  def __init__(self,data,nextnode=None):
    self.data=data
    self.next=nextnode

def k_point(link_list,k):
  #输入的K不正确，比链表都长
  #链表为空
  #k不是数字
  #由于link_list是我自己构造的，不存在链表错误的问题。
  k_point=link_list
  if not isinstance(link_list,Node):
    return link_list.__class__.__name__+" is not Node"
  if not str(k).isdigit():
    return "k is not right input"
  for i in range(k-1):
    if k_point.next is not None:
      k_point=k_point.next
    else:
      return "K不正确"
  
  while k_point.next is not None:
    k_point,link_list=k_point.next,link_list.next
  return link_list.data
def constructor(arr):
  head=Node(arr[0])
  p=head
  for i in range(1,len(arr)):
    p.next=Node(arr[i])
    p=p.next
  return head

print("first test :",k_point(constructor([1,2,3,4,5,6,7,8,9]),'a'))  

print("second test :",k_point([],'a'))  