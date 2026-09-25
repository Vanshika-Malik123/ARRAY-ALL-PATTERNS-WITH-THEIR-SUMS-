#Fixed-Size Sliding Window — 6-Line Summar
# Use a sliding window to process consecutive elements without recalculating everything.
# right expands the window, and left moves it forward.
# Calculate the window size using right - left + 1.
# When the window size becomes k, process it (sum, average, maximum, minimum, etc.).
# After processing, remove nums[left] and increase left by 1.
# Pattern: Expand → Check size → Process → Remove left → Slide.
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_avg=0
        left=0
        right=0
        max_avg=float('-inf')# here max_avg = 0 it can also be used but with this it only pas 121/128 test case with this float we can also put negative numbers here 
#Maximum of possibly negative numbers → float('-inf') 
#Minimum of possibly positive numbers → float('inf')
        for right in range (len(nums)):
            window_avg+=nums[right]
            if right-left+1==k:
                max_avg = max(max_avg, window_avg / k)
                window_avg-=nums[left]
                left+=1
        return (max_avg)
        