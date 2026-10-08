class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        ans = [-1] * len(nums2)
        # Find NGE for nums2
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums2[i])
        # Convert nums2 answers into HashMap
        greater = {}
        for i in range(len(nums2)):
            greater[nums2[i]] = ans[i]
        # Find answers for nums1
        result = []
        for num in nums1:
            result.append(greater[num])
        return result