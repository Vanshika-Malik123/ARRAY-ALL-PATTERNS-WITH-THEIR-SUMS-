# Bruteforce without two pointers could not passes few testcases
# class Solution:
#     def findDuplicate(self, nums: list[int]) -> int:
#         nums.sort()
#         for i in range(len(nums)):
#             nums[i]==nums[i]
#             nums.remove(nums[i])
#             return nums[i]
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        nums.sort()

        left = 0
        right = 1

        while right < len(nums):

            # If two neighboring values are same,
            # we found the duplicate.
            if nums[left] == nums[right]:
                return nums[left]

            # Move both pointers forward
            left += 1
            right += 1