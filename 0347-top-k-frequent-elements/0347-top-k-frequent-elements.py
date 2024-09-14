import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        Using arrays instead of the heaps
        Time Complexity O(N) optimised from that of heaps that process in the order of O(N+UlogU+klogU)
        Space Complexity O(N) tradeoff for faster processing compared to heaps that requires O(U) order space
        '''
        #create a hashmap of unique numbers occuring in the list and their frequency
        freqMap = {}
        for i in nums:
            currFreq = freqMap.get(i,0)
            freqMap[i] = 1 + currFreq
        
        #Now create 2D list, to store all the values having a frequency at a index equals to the frequency. Max Freq can be 'len(nums)' when all the array elements are same. Minimum frequency can be '1'
        freqEle2DList = [[] for i in range(len(nums)+1)]

        #iterate over the dictionary to fill the 2D list
        for val,freq in freqMap.items():
            freqEle2DList[freq].append(val)

        #Now over the 2D list from back to get top k frequent elements
        result = []
        for i in range(len(nums),0,-1):
            for j in freqEle2DList[i]:
                result.append(j)
                if len(result) == k:
                    return result
        
        return result