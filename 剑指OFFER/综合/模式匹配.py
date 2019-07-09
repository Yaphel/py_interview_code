def pattern_match(str1,pattern):
  str1_len=len(str1)-1
  pattern_len=len(pattern)-1
  s=p=0
  while s<str1_len and p<pattern_len:
    if p+1<pattern_len :
      if pattern[p+1]=='*':
        while str1[s]==pattern[p]:
          s+=1
        p+=2
      else:
        if str1[s] == pattern[p]:
          s+=1
          p+=1
        else:
          return "error"
    else:
      if str1[s] == pattern[p]:
        return "error"
  if s==str1_len and p==pattern_len:
    return "fine"
  else:
    return "error"

print(pattern_match('abcca','ab*c*a'))
print(pattern_match('abc','a*b'))    
