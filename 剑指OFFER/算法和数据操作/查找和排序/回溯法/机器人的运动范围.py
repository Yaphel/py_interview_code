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
    
def check_not_overflow(x,y,overflow_number):
  if count_number(x)+count_number(y)<overflow_number:
    return True
  return False
  
def count_number(number):
  count=0
  while number>0:
    count+=number%10
    number=number//10
  return count

def has_path(v_list,pointx,pointy,n,overflow_number,count =0):
  if 0<=pointx<n and 0<=pointy<n and check_not_overflow(pointx,pointy,overflow_number) and is_not_visited(n*pointx+pointy,v_list) :#无碰撞和访问
    #print("now:",pointx,pointy)
      v_list.add(pointx*n+pointy)
      print("push point:" ,pointx,pointy)
      count+=1
      print("now count:" ,count)
      return max(has_path(v_list,pointx,pointy+1,n,overflow_number,count),has_path(v_list,pointx,pointy-1,n,overflow_number,count),has_path(v_list,pointx+1,pointy,n,overflow_number,count),has_path(v_list,pointx-1,pointy,n,overflow_number,count))
  else: 
    return count

def find_path(n,overflow_number):
  arr=arr_constructor(n)
  max_point=0
  v_list=set()

  now=has_path(v_list,0,0,n,overflow_number)

  return now
if __name__ == '__main__':
  print(find_path(20,5))  
  
