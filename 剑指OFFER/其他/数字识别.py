#允许输入的类型：
a=['+','-']
b=['1','2','3','4','5','6','7','8','9']
c=['0']
d=['.']
e=['e','E']

def judge(a,b):
  if a in b:
    return True
  else:
    return False
def recongnize_digit(arr,f1 =0):
  arr_len=len(arr)
  if arr_len is 0:
    return "error!"
  if judge(arr[0],a) or judge(arr[0],b):
    for i in range(1,arr_len):
      if judge(arr[i],e) and f1 is not 1:
        f1=1
        return recongnize_digit(arr[i+1:],f1)
      else:
        if judge(arr[i],b) or judge(arr[i],c):
          pass
        elif judge(arr[i],d) and f1 is not 1:
          f1=1
          return recongnize_digit(arr[i+1:],f1)
        else:
          return "error!"
  return "OK!"

print(recongnize_digit('+100'))
print(recongnize_digit('5e2'))
print(recongnize_digit('-123'))
print(recongnize_digit('3.123'))
print(recongnize_digit('-1E-16'))
print(recongnize_digit('12e'))
print(recongnize_digit('1a3.14'))
print(recongnize_digit('1.2.3'))
print(recongnize_digit('+-5'))
print(recongnize_digit('12e+5.4'))