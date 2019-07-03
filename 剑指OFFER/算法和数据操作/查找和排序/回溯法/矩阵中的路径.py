class Stack(object):
  s=set()
  dream_land=set([1,2,3,4])
  def __init__(self,data,way = -1):
    self.direction=[0,0,0,0]
    self.next=None
    self.data=data
    self.way=-1
    # -1:init 0:up 1:down 2:left 3:right
    self.before=None
  def pop(self):
    way=self.way
    if way is -1:
      return "change start"
    self.before.direction[way]=1
    s.remove(self.data)
    return self.before
  def go(self):
    if self.direction is [1,1,1,1]:
      return "cant go"
    for i in range(4):
      if self.direction[i] is 0:
        newdata=next_step(self.data,i)#下一步
        if newdata is False or check_done(newdata,s):#
          self.direction[i]=1
        else:
          new=Stack(newdata,i)
          new.before=self
          self.next=new
          s.add(self.data)
          if check_ok(s,dream_land):
            return True
          s.go() #否则继续征程

def check_ok(set1,set2):
  if set2 in set1:
    return True
  return False

def check_done(point,set1):
  if point in set1:
    return "cant pass"
  else:
    return "pass"

def next_step(data,direction):
  data1=data//4
  data2=data % 4
  if data1 is 0 and direction is 0:
    return False
  if data1 is 3 and direction is 1:
    return False
  if data2 is 0 and direction is 2:
    return False
  if data2 is 3 and direction is 3:
    return False

def find_path_in_matrix(matrix,path):
  for i in path:#任意起点
    s=Stack(i)
    while 1:
      a=s.go()
      if a:
        return "finally, we find a path."
      else:
        break


import unittest

class MyTest(unittest.TestCase):
  def test_01(self): 
    matrix=[
      [0,1,2,3],
      [4,5,6,7],
      [8,9,10,11],
      [12,13,14,15]]
    print(find_path_in_matrix(matrix,set([1,2,3,4])))
if __name__ == '__main__':
  unittest.main()
