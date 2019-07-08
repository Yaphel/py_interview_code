def greed_is_good(n):
  if n>=5:
    return 3*greed_is_good(n-3)
  else:
    return n

print(greed_is_good(8))

#若计算得当，这种方法省时省力。