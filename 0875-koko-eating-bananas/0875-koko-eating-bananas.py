import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        '''
        We have to find a number k, such that 1 <= k <= max(piles) and helps koko to eat all bananas.

        1 <= piles[i] <= 10^9 so 1 <= k <= 10^9 in general
        We will have a huge range to search for the k. Again for each k, to verify if koko each k bananas in an hour, will koko be able eat all bananas which might take O(N) order of time (where N is length of piles array i.e, number of piles)
        If we take each number in the range of k as k and verify if it is a feasible k, then the time complexity would be of order O(max(piles))*O(len(piles)) 
        In worst case the time taken would be O(10^9)*O(10^4) = O(10^13)
        This approach exceeds the time limit of 10^7
        Brute force approach
            Time Complexity - O(N*M)
            Space Complexity - O(1)
            where M is max number of bananas in a pile.

        Optimsing Approach
        We know k is bounded by in a range, so why not try using binary search instead of linear search.
        Because, if we use binary search to find k, the time complexity of finding a k will reduce from linear order O(max(piles)) to log order O(log(max(piles)))
        This will inturn reduce total time complexity to O(log(max(piles)))*O(N).
        
        Time Complexity - O(NlogM)
        Space Complexity - O(1)
        where M is max number of bananas in a pile.

        Intution behind this approach is Binary search can be used to find a number between two bounds and if we have a mechanism to move left & right bounds after each search (ie., l = mid+1 or r = mid-1) 
        '''

        l, r = 1, max(piles)
        res = r

        while l<=r:
            temp_k = int(l + (r-l)//2)
            temp_h = 0
            for p in piles:
                temp_h += int(math.ceil(float(p)/temp_k))
            
            if temp_h > h:
                l = temp_k+1
            else:
                res = temp_k
                r = temp_k-1
            
        return res
        
            

