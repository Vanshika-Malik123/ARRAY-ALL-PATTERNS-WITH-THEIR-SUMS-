
# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         for i in range(len(nums)):
#             nums[i] = nums[i] ** 2

#         nums.sort()
#         return nums
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        result.reverse()
        return result
