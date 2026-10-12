# peak index in mountain array question main conditin here is arr[mid]<arr[mid]-1
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low