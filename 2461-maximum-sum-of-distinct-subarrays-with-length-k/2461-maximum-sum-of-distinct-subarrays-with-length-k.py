class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        left = 0
        window_sum = 0
        max_sum = 0
        count = {}
        for right in range(len(nums)):
            # Add right element
            window_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            # Window size = k
            if right - left + 1 == k:
                # All elements are distinct
                if len(count) == k:
                    max_sum = max(max_sum, window_sum)
                # Remove left element
                window_sum -= nums[left]
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return max_sum