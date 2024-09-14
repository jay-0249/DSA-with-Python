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
        
        numListWithFreq = [(-freq, num) for num,freq in countNum.items()]

        heapq.heapify(numListWithFreq)

        result = [heapq.heappop(numListWithFreq)[1] for _ in range(k)]
        # for i in range(0,k):
        #     result[i] = heapq.heappop(numListWithFreq)[1] 
        
        return result

