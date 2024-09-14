import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        countNum = {}

        for i in nums:
            countNum[i] = 1 + countNum.get(i,0)
        
        numListWithFreq = [(freq, num) for num,freq in countNum.items()]

        result = [num for freq, num in heapq.nlargest(k, numListWithFreq)]
        
        return result

