# This is the classic example of two pointers here what happen is i pointer remin fix and j and k pointers move . so treat j as left pointer and k as right pointer now do similar to two sum like sum==0 so nums[i]+nums[j]+nums[k]==0 if they are equal to zero then append it into resukt . if sum is greater than zero than k-=1 if sum is less then 0 then j+=1 then at last return the result

###     Briteforce approach it will solve in O(n^3)but woth optimixw it willl solve in O(n^2)
# class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []

    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     result.append([nums[i], nums[j], nums[k]])

    #     return result


# here in optimized approach ex[1,0,2,0,-1,-1,3,2,0,1 so here i jk three pointer are there where i is stable and j an dk works as left and right 
#so i is from len(nums)-2 ,0 and j is from j=1 to len(nums)-1 and k is k=2 to len(nums)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
#Here after sorting we used set function so the result does not caontain any deuplicte value but keep in mind at last conver this set into list 
# using 
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    # since i am using set for removing suplciate then instead of append i must use add and since i am using add so i must convert my list into tuple 
                    # before it is result.append([nums[i],nums[j],nums[k]]) but now list in tuple
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return [list(x) for x in result] # it is just a way to do with tuple into list 
