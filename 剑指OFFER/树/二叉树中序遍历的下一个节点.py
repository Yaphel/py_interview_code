class TNode(object):
    def __init__(self,data,lc = None,rc = None,parent = None):
        self.data = data
        self.lc = lc
        self.rc = rc
        self.parent = parent #很显然没有父节点的节点即为根节点。

#建立树
def constructor(before,middle,parent = None):#寻找树的根节点
  if len(before) is not 0:
    node=TNode(before[0])
    node.parent=parent
    trans=find_number_in_m(before[0],middle)
    node.lc=constructor(before[1:trans+1],middle[0:trans],node)
    node.rc=constructor(before[trans+1:],middle[trans+1:],node)
    return node
  else:
    return None

def find_number_in_m(left_number,middle):
  for i in range(len(middle)):
    if left_number is middle[i]:
      return i 
  return None #输入有误

#寻找树的下一个中序遍历节点
def find_next_node_in_tree(root,data):
  node=find_node_in_tree(root,data)
  rflag=0
  while 1:
    if node.rc is not None and rflag==0:
      #返回右子树的中序遍历的第一个节点。
      node=node.rc
      return find_first_in_middle(node)
    else:
      rflag=0
      if node.parent is None:
        print("not found")
        return None
      if node.parent.lc is node:#是父节点的左子树。
        return node.parent.data
      else:#不是左树，有父节点，肯定是右子树。
        node=node.parent#问题升级。
        rflag=1
        

# 这段代码有个细节：因为不是遍历而是查找，在遍历的时候不能返回None。
# 所以我在这里加了个判断        
def find_node_in_tree(node,data):
  if node is not None:
    if node.data==data:
      return node
    if node.lc is not None:
      current_node=find_node_in_tree(node.lc,data)
      if current_node is not None:
        return current_node
    if node.rc is not None:
      current_node=find_node_in_tree(node.rc,data)
      if current_node is not None:
        return current_node
  else:
    return None

def find_first_in_middle(node):
  if node.lc is not None:
    return find_first_in_middle(node.lc)
  else:
    return node.data
import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    print(find_next_node_in_tree(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]),8))
    #print(find_node_in_tree(constructor([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]),8).data)
if __name__ == '__main__':
  unittest.main()