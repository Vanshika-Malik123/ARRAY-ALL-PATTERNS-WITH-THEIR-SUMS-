#oky so this question is of same direction pointer(remeber same direction both pointer remins at index 0
#one alwasy wrks like for loop jusr define lrft and right then use for loops and then define conditions according to question here since we have to move all the zeroes toward right so we use swap to swap all zeroes toward right )

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left=0
        right=len(nums)
        for right in range (len(nums)):
            if nums[right]!=0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right+=1


        """
        Do not return anything, modify nums in-place instead.
        """
        