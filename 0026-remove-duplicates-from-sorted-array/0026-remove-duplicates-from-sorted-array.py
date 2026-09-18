# okay so this question is easy here simple whats happening we dont care if 1==1 on similar element we are not doing anything but 
# if i=j so we got anew elemnt here right so 
# j will say to i bhai i got a new element here 
# then i will say ok bhai i will make space for that new elemnt so i++
# now i had make a spce so we will put that j value in i means nums[i]=nums[j]
# now j will again move to find a new elemtn and similarly if i and j are equal nothung j move forward but agin if j got new elemtn then i will make space and gonna interchage their values .
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        right = 1
        while right<len(nums):

            if nums[left] != nums[right]:
                left+=1
                nums[left]=nums[right]
            right+=1
        return left+1