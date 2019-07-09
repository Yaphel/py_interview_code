#之字形不写了。实现太简单了。只需要把print独立成一个打印函数，在里面加逻辑即可。这里面涉及到了扩展性的思想。
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

def print_tree(node):
  arr=[]
  arr.append(node)
  while 1:
    arr=print_tree_layer(arr)
    if arr is "end":
      return arr
def print_tree_layer(arr):
  arr1=[]
  for i in arr:
    print(" ",i.data,end="")
    if i.lc is not None:
      arr1.append(i.lc)
    if i.rc is not None:
      arr1.append(i.rc)
  print("-------------------------")
  if len(arr1) is 0:
    return "end"
  else:
    return arr1
print_tree(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))