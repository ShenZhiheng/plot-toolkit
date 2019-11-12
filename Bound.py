#coding=utf-8
# author: zhShen
# date: 20190920
#返回nums中第一个>=target的值得位置，如果nums中都比target小，则返回len(nums)
def lower_bound(nums, target):
    low, high = 0, len(nums)-1
    pos = len(nums)
    while low<high:
        mid = (low+high)/2
        if nums[mid] < target:
            low = mid+1
        else:#>=
            high = mid
            #pos = high
    if nums[low]>=target:
        pos = low
    return pos



#返回nums中第一个>target的值得位置，如果nums中都不比target大，则返回len(nums)
def upper_bound(nums, target):
    low, high = 0, len(nums)-1
    pos = len(nums)
    while low<high:
        mid=(low+high)/2
        if nums[mid]<=target:
            low = mid+1
        else:#>
            high = mid
            pos = high
    return pos