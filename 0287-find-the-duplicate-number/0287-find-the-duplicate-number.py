# class Solution:
#     def findDuplicate(self, nums: list[int]) -> int:
#         for i in range(len(nums)):
#             nums[i]==nums[i]
#             nums.remove(nums[i])
#             return nums[i]
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        left = nums[0]
        right = nums[0]

        # Find the meeting point
        while True:
            left = nums[left]          # moves 1 step
            right = nums[nums[right]]  # moves 2 steps

            if left == right:
                break

        # Find the entrance of the cycle
        left = nums[0]

        while left != right:
            left = nums[left]
            right = nums[right]

        return left