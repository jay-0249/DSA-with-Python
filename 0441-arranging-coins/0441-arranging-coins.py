class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        The length of rows forms a series (Arithmetic Progression Series) starting from 1 with a difference of 1 between successive numbers
        1,2,3,4,....
        The last row can be incomplete
        let k be the number of complete rows
        Sum of k terms = k(k+1)/2
        Sum of k+1 terms = (K+1)(k+2)/2
        n coins can make k complete rows on whole or k complete rows with some coins less than that of the required coins to make another row(k+1)
        so, k(k+1)/2 < n < (K+1)(k+2)/2
        for k = 2^16, k(k+1)/2 = (2^16)*(2^16+1)/2 = 2^31 + 2^15
        for k = 2^16-1, k(k+1)/2 = (2^16 - 1)*(2^16)/2 = 2^31-2^15
        that is to complete 2^16 rows, we will require 2^31 + 2^15 coins, but the maximum number of coins we can have is 2^31 - 1
        but to complete 2^16 - 1 rows, we will require 2^31 - 2^15 coins which can be possible number of coins we can have
        Therefore the maximum number of rows for the staircase, we can build is 2^16 - 1 rows.
        Using Binary Search, search for such a 'k' (complete rows) for a given 'n' coins such that k(k+1)/2 < n < (K+1)(k+2)/2
        '''
        if n >= 2**31-2**15:
            return 2**16-1

        def numberOfCoinsRequired(k):
            return k*(k+1)/2

        l, r = 0, 2**16-2
        while l<=r:
            mid = l+(r-l)/2

            coinsNrows = numberOfCoinsRequired(mid)
            if n == coinsNrows:
                return mid
            elif n<coinsNrows:
                r = mid-1
            #n > numberOfCoinsRequired(mid) and n < numberOfCoinsRequired(mid+1) that with the coins we have, we can make 'mid' complete rows and let with some coins that are not enough to build 'mid+1' row
            elif n<numberOfCoinsRequired(mid+1):
                return mid
            else:
                l = mid+1
        
        return n
