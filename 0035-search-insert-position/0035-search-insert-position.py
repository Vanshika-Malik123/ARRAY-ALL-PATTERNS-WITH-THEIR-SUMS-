#        return mid + 1 if target > nums[mid] else mid
# most important line in thsi question if i dont find the target then the target should be add nex to mid means mid+1 and elese return mid

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]==target:
                return mid
            else:
                high=mid-1
                
        return mid + 1 if target > nums[mid] else mid

        