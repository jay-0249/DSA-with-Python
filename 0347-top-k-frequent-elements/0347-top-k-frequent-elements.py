import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #create a hashmap of unique numbers occuring in the list and their frequency
        freqMap = {}
        for i in nums:
            currFreq = freqMap.get(i,0)
            freqMap[i] = 1 + currFreq
        
        #We need a data structure to sort the frequencies faster and also access the top k frequent elements
        tupleList = [(-freq,val) for val,freq in freqMap.items()]
        
        #Transform the list of tuples as heap
        heapq.heapify(tupleList)
        
        #Extract the top k frequent elements
        result = [heapq.heappop(tupleList)[1] for i in range(0,k)]

        return result
    
