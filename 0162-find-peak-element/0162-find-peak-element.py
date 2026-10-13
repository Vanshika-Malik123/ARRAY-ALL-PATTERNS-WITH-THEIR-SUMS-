#mostly for peak elemnt this same template follows like if mid is greater then mid+1 high=mid and if mid is smaller than mid+1 then low=mid+1
# mid and mid+1 comaprison is alwasy happen in these peek type of question because mostly in peek elemnt we have to consider strictly greater than a neighbour that is outside the array

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:           
                high=mid
            else:
                low=mid+1
        return high
            

            
        