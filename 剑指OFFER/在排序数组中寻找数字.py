#这个题实际上是二分查找的变体。
#但我认为书上的思路有优化空间。
#我的想法是首先确认数组的内容。如果是整数。那就好说了。
#如果我想要查找[1,2,3,3,3,3,3,3,3,4]中3的次数。我可以直接查找2.9和3.1的位置。调整算法，若不出现则返回旁边的值。
#相减自然可以求得了。速度会快一点点。

#书上没有做这种假设，直接修改二分，查找最前面和最后面的数字。
#最后也是相减。