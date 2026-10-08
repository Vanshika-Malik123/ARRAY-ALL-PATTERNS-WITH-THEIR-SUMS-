class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        ans = [-1] * len(nums2)
        # Find next greater for nums2
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums2[i])
        # Get answers for nums1
        result = []
        for num in nums1:
            i = nums2.index(num)
            result.append(ans[i])
        return result