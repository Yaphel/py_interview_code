def biggest_income(arr):
  start_at=arr[0]
  max_income=0
  now_income=0
  for i in range(1,len(arr)-1):
    now_income+=arr[i]-arr[i-1]
    if now_income<0:
      start_at=arr[i]
      now_income=0
    if now_income>max_income:
      max_income=now_income
  return [max_income,start_at]

print(biggest_income([9,11,8,5,7,12,16,14]))