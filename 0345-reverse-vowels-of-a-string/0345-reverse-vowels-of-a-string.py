class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Reverse the vowels only by swaping characters
        Using two pointers iterate from start and end, checking if the character at the pointers is vowel or not.
        If yes, assign the respective Boolean to true else we should move to next character for that pointer (+=1 for start, -=1 for end)
        At each iteration swap if both pointers are pointing to a Vowel character else continue
        Proceed to iterate this way until start<end
        Booleans initial value before iteration should be False
        """
        start = 0
        end = len(s)-1
        isStartVowel = False
        isEndVowel = False
        vowels = ['a','e','i','o','u']
        #Convert string into list as 'unicode' object - string is immutable
        #Fun fact: Tuple is not a unicode object but is immutable in python
        #list(s) or s.split(), slist = [x for a,x in enumerate(s)]
        sList = [x for x in s]
        while start < end:
            if s[start].lower() in vowels:
                isStartVowel = True
            else:
                start += 1
            if s[end].lower() in vowels:
                isEndVowel = True
            else:
                end -= 1
            if isStartVowel and isEndVowel:
                temp = sList[start]
                sList[start] = sList[end]
                sList[end] = temp
                start += 1
                isStartVowel = False
                end -= 1
                isEndVowel = False
                
        return ''.join(sList)