def arr_constructor(n):
  arr = []
  for i in range(n):
    for j in range(n):
      arr.append(i*n+j)
  return arr

def is_not_visited(n,v_list):
  if n in v_list:
    return False
  return True
    
def has_path(path_set,v_list,pointx,pointy,n):
  if 0<=pointx<n and 0<=pointy<n and is_not_visited(n*pointx+pointy,v_list):#无碰撞和访问
    #print("now:",pointx,pointy)
    v_list.add(pointx*n+pointy)
    has_done=0
    if path_set.issubset(v_list):
      has_done=1
    if has_done:
      return True
    else:
      return has_path(path_set,v_list,pointx,pointy+1,n) or has_path(path_set,v_list,pointx,pointy-1,n) or has_path(path_set,v_list,pointx+1,pointy,n) or has_path(path_set,v_list,pointx-1,pointy,n)

def find_path(arr,path,n):
  for i in path:
    #init
    v_list=set()
    path_set=set(path)
    pointx=i//n
    pointy=i%n
    if has_path(path_set,v_list,pointx,pointy,n):
      return v_list
  return 0
if __name__ == '__main__':
  print(find_path(arr_constructor(4),[0,4,8,11],4))

