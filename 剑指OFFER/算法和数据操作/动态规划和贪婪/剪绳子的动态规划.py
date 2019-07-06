def cut_rope(n,number):
  if n==1 and n==0:
    return 1
  if n==2:
    return 2
  for i in range(2,((n+1)//2)+1):
    print("cut:",i,"left:",n-i)
    rtn.append(cut_rope(n-i)*i,number)
  return number

print(cut_rope(8))