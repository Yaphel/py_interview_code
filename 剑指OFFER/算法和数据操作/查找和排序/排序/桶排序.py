def bucket_sort(arr,start,end,bucketnumber):
  bucket=[]
  for i in range(bucketnumber):
    bucket.append([])
  piece=(end-start)//bucketnumber
  for i in arr:
    point=(i-start)//piece
    bucket[point].append(i)
  rtn=concat_bucket(bucket,bucketnumber)
  return rtn
 
def concat_bucket(bucket,bucketnumber):
  rtn=[]
  for i in bucket:
    i.sort()
    rtn=rtn+i
  return rtn

print(bucket_sort([9,8,7,6,5,4,3,46,5,4,2,4,5,6,3,2,34,5,5,5,3,3],0,50,10))