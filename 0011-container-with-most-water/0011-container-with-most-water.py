# ## Container With Most Water — Quick Revision
#  **Problem:** Given heights of vertical lines, choose two lines that hold the **maximum amount of water**.
#  ### Core idea
#  Use **two pointers**:
# ```
# left → beginning
# right → end
# ```
#  The container is like a rectangle:
# ```
# Area = width × height
# ```
#  So:
# ```
# width  = right - left
# height = min(height[left], height[right])
# ```
#  Therefore:
# ```
# area = (right - left) × min(height[left], height[right])
# ```
#  ### Why move the shorter pointer?
#  The **shorter line limits the water level**.
#  Example:
# ```
# left = 8
# right = 5
# water height = 5
# ```
#  If you move the taller line (`8`), the width decreases but the height **cannot increase**, because the `5` is still limiting it.
#  So:
#  > **Always move the pointer pointing to the shorter line.**
#  If both are equal, move either one.
#  ### Pseudocode
# ```
# left = 0
# right = n - 1
# max_area = 0
# while left < right:
#     width = right - left
#     water_height = min(height[left], height[right])
#     area = width × water_height
#     max_area = max(max_area, area)
#     if height[left] < height[right]:
#         left++
#     else:
#         right--
# return max_area
# ```
#  ### Complexity
# ```
# Time  → O(n)
# Space → O(1)
# ```
#  ### Remember this
#  **"Start at both ends → calculate area → move the shorter line → keep maximum."**

#  For the example:

# ```
# [1,8,6,2,5,4,8,3,7]
# ```

#  The maximum comes from:

# ```
# index 1 → height 8
# index 8 → height 7

# width = 8 - 1 = 7
# height = min(8,7) = 7

# area = 7 × 7 = 49
# ```

#  **Pattern:** `Two Pointers` → **opposite ends + move smaller**.
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])

            if area > max_area:
                max_area = area
# if height[left]>height[right]
            #right+=1
            

            
            if height[left] < height[right]:   
                left += 1
            else:
                right -= 1

        return max_area


