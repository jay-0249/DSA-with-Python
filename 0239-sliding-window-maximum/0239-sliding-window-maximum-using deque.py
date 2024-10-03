import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        slide over the iterable array, find something(max) in each window -> sliding window

        we want to find maximum in each window in least time -> heap would be the data structure to return the maximum value in least time O(log w) where w is the length of window

        add these maximums into a array and return
        

        if len(nums) < k:
            return []

        result = []

        max_heap = []

        #add first k-1 characters into max_heap
        for i in range(0,k-1):
            heapq.heappush(max_heap, -1*nums[i])

        #iterate from the k th character
        for current in range(k-1,len(nums)):
            #push current character
            heapq.heappush(max_heap, -1*nums[current])
            #get max character in the current window and add to result
            result.append(-1*max_heap[0])
            #remove the starting character of the window
            max_heap.remove(-1*nums[current-(k-1)])
            heapq.heapify(max_heap)
        
        return result
        '''
        dq = collections.deque()
        result = [0]*(len(nums)-k+1)

        for i, num in enumerate(nums):
            #remove if the max element is out of the window
            if dq and dq[0] < i-k+1:
                dq.popleft()
            #remove numbers that less than the current number
            while dq and nums[dq[-1]] < num:
                dq.pop()
            #append current element index
            dq.append(i)
            #fetch the maximum number for this window
            if i > k-2:
                result[i-k+1] = nums[dq[0]]
        
        return result


