class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
            
        first_element = nums[0]

        # First half loop: Only runs if the target belongs to the larger left side
        low = 0
        high = n - 1
        while low <= high and target >= first_element:
            index = (low + high) // 2
            
            if nums[index] == target:
                return index
            
            # If we drift into the smaller second half, push high back left
            if nums[index] < first_element:
                high = index - 1
            elif nums[index] < target:
                low = index + 1
            else:
                high = index - 1

        # Second half loop: Only runs if the target belongs to the smaller right side
        low = 0
        high = n - 1
        while low <= high and target < first_element:
            index = (low + high) // 2
            
            if nums[index] == target:
                return index
                
            # If we drift back into the larger first half, push low forward right
            if nums[index] >= first_element:
                low = index + 1
            elif nums[index] < target:
                low = index + 1
            else:
                high = index - 1

        return -1
