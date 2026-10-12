# this is basic binary search question which follow basic binary search template like if mid element eqals to target it return mid and if mid element smaller than see to right side and increase left and if mid element is larger than look at right side and subtract 
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]==target:
                return mid
            else:
                right=mid-1
        return -1