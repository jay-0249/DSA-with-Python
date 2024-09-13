class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        resultDict = {}

        for i in strs:
            sortedStr = ''.join(sorted(i))
            if sortedStr in resultDict:
                resultDict[sortedStr].append(i)
            else:
                resultDict[sortedStr] = [i]

        return resultDict.values()