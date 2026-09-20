### Dutch National Flag Algorithm

# The Dutch National Flag algorithm sorts an array containing three different values using three pointers: `low`, `mid`, and `high`.

# * `low` → position where the next `0` should go.
# * `mid` → checks the current element.
# * `high` → position where the next `2` should go.

# **Rules:**

# * If `nums[mid] == 0`: swap with `low`, then increase both `low` and `mid`.
# * If `nums[mid] == 1`: increase `mid` only.
# * If `nums[mid] == 2`: swap with `high`, decrease `high`, but **do not increase `mid`** because the new element at `mid` has not been checked yet.

# This sorts the array in **O(n) time** and **O(1) extra space**.

class Solution:
    def sortColors(self, nums: list[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1