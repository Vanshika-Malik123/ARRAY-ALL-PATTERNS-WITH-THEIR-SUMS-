#this question main concern is that we ahve to revere a string inplace means we dont have to make another list and store it there 
# so here i had used SWAP function just simple swap left and right 

# its time complaexity is O(n)
# space complecity is O(1)

#optimised approach 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1

# bruteforce approach but here the timecomplecity is O(n) and sapce complexity is also O(n)

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         reversed_s = s[::-1]

#         for i in range(len(s)):
#             s[i] = reversed_s[i]
