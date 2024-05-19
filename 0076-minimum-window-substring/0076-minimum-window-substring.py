class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        Create a dictionary of the elements in the string 't' with their respective frequency.
        Use a counter as a count of all elements of 't'.
        Now using two pointers begin, end. Slide through the string 's' to find a substring between start and end pointers such that it contains all the elements of 't' (matching with the element repetition as that of 't')
        You can check this using a counter(size of 't'), whenever you find a matching element in 's', check if we were still required to find such an element in string 's' (dictT[char]>0), decrement the local counter. (also decrement the dictT[char])
        So when local counter is zero, it means that we have found a substring that has all elements as that of string 't'
        Now let's try to check if the begining character is an element in string 't' or not. If not, increment the begin pointer
        '''

        #check if 's' contains atleast equal or more than number of characters to that of string 't'
        if len(s) < len(t):
            return ""
        #create a result sub-string
        resultSubstring = ""

        #create a dictionary of elements in string 't' and their respective frequency
        dictTelements = dict()
        for ele in t:
            #if dictTelements.get(ele):    it is better to use 'in operator' bcz if dictTelements.get(ele) fails when get() returns '0'. Eventhough is not a possibility in our case, better to follow 'in' operator
            if ele in dictTelements:
                dictTelements[ele] = dictTelements[ele]+1 
            else:
                dictTelements[ele] = 1
        
        #start sliding through the string 's'
        begin, end = 0, 0
        counterS = len(t)

        #Until the end pointer is in bounds of string 's'
        while end < len(s):
            #as we do not have scenario that string 't' can be an empty string, we do not check if the counter is zero prior initially rather we can check if the current character is a character that is in 't'
            currentChar = s[end]
            #check if this char is still required to make it a substring that contains all characters of string 't'
            if dictTelements.get(currentChar) > 0:
                counterS -= 1
            #check if this char is in dictionary
                #there can be a case where we can the frequency of currentChar (in dictionary) is zero or less than zero, which means we do not require that character to make the substring of 's' a required substring. But we still have to account for that element for sliding window(if that element is present as an element of string 't') and thereby decrease the frequency of the element. so check if this char is in dictionary
            if currentChar in dictTelements:
                dictTelements[currentChar] = dictTelements[currentChar] - 1

            #Increase the window right end by moving the right end to the next character
            end += 1

            #Check if the substring between pointers 'begin' and 'end' contains all elements of 't'
            while counterS == 0 :
                #check if this substring is smaller to that of the previous shortest substring that conatins all elements of 't'
                if end - begin < len(resultSubstring) or resultSubstring == "":
                    resultSubstring = s[begin:end:1]
                #Check if the begin element is in dictTelements
                #As we move to slide the window from 'begin' to next element, we will have to find such an element again in the string 's' to be a substring that contains all elements of string 't'
                if s[begin] in dictTelements:
                    dictTelements[s[begin]] += 1
                    if dictTelements[s[begin]]>0:
                        counterS += 1
                
                begin += 1
            
        return resultSubstring
