#this question can be solved by using two  approaches first one is two pointer and second is dutch national flag 
# this is the first approach here using two pointer pattern 
# class Solution:
#     def sortArrayByParity(self, nums: list[int]) -> list[int]:
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             if nums[left] % 2 == 0:
#                 left += 1
#             elif nums[right] % 2 == 1:
#                 right -= 1
#             else:
#                 nums[left], nums[right] = nums[right], nums[left]
#         return nums
  # thus is solved by dnf 
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] % 2 == 0:       # even
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            else:                         # odd
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums