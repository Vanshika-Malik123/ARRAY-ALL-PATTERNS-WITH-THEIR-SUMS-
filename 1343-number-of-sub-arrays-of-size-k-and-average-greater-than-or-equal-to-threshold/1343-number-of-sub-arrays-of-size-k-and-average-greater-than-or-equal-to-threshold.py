# this is the classic example of fixed sliding window in sliding widow everyhting always remain same untill right-left+1==k if its simple sliding window question where there is no dictionary or no distict elemtn type problem or if we hae to find number of subarray use count to caluclate the subarray like how many subarrays follows that particular condiditon jus tlike this subarray wher average is greater or equal then the threshhold 
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left=0
        windowsum=0
        maxavg=0
        count=0
        for right in range (len(arr)):
            windowsum+=arr[right]
            if right-left+1==k:
                if windowsum/k>=threshold:
                    count+=1
                windowsum-=arr[left]
                left+=1
        return count
        