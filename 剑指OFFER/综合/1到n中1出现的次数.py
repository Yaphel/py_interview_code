def count1(number):
#  if len(number) is 1:
#    if int(number) is 1:
#      return 1
#    else:
#      return 0
#  if number[0] is '1':
#    return int(str[1:])+count1(number[1:])+count1('9'*(len(number)-1))+1
#  else:
#    return (int(number[0])-2)*count1('9'*(len(number)-1))+count1(number[1:])+count1('1'+'9'*(len(number)-1))
  if number<1:
    return "error input"
  if number<10:
    return 1
  
  [first_number,count]=get_first_number(number)
  other_number=get_other_number(number,first_number,count)
  if first_number is 1:
    return other_number+1+count1(get_9(count-1))
  else:
    return (first_number-1)+get_9(count-1)+1+count1(other_number)
# 取得最前面的数字。
def get_first_number(number):
  count=1
  while number//10 is not 0:
    count+=1
    number=number//10
  return [number,count]

def get_other_number(number,first_number,count):
  for i in range(count-1):
    first_number*=10
  return number-first_number

def get_9(count):
  rtn=0
  for i in range(count):
    rtn=rtn*10+9
  return rtn

print(count1(100))