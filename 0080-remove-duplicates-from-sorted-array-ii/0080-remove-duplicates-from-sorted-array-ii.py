#if left < 2:
#Always allow the first two numbers.
#nums[right] != nums[left - 2]
# means:
# "Is this number different from the number two positions behind in my result?"
# If yes → keep it.
# If no → it's the third or later occurrence, so skip it.
# Example
# Input:
# [0,0,1,1,1,1,2,3,3]
# Output portion:
# [0,0,1,1,2,3,3]
# left is the pointer that builds the valid answer.
# right is the pointer that scans every element.


 class Solution:
     def removeDuplicates(self, nums: list[int]) -> int:
         left = 0

        for right in range(len(nums)):
            if left < 2 or nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1

        return left




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index
        
