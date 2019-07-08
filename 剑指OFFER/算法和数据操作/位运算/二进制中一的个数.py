def number_of_one(n):
  count=0
  while n is not 0:
    count+=1
    n=n & (n-1)
  return count

print(number_of_one(0b01111111111111111111))
