#whenever solving sliding window always see k #In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards. since here the question is k cards exactly (one card fdrom begnning and another card from end ) so here beginnign is total length which is len(acrdpoints0-k so wwe will get middel elements here)
# "What does k represent in this question?" ✅

# Question wording	k means	Window
# "subarray of size k"	window size	k
# "subarray of length k"	window size	k
# "take k consecutive elements"	window size	k
# "take k cards from beginning/end"	cards taken	n-k
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left = 0
        windowsum = 0
        minsum = float('inf')
        if k == len(cardPoints):
            return sum(cardPoints)
        for right in range(len(cardPoints)):
            windowsum += cardPoints[right]
            if right - left + 1 == len(cardPoints) - k:
                minsum = min(minsum, windowsum)
                windowsum -= cardPoints[left]
                left += 1
        return sum(cardPoints) - minsum