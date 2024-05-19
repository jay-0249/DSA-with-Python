class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        '''
        We can start filling from the first tree. We can use a 'dict' data structure to keep track of the fruits we are filling the baskets with and respective the number of trees from which we have taken a fruit type.
        
        While moving forward, add the type of fruit and update it's count we have taken in the 'dict' data structure. Then, if we have less than or equal to 2 types of fruits, move forward, else if type(fruits) > 2, we have to change our begining tree to a tree such that the type of fruits is less than, in this process of moving the begining tree to next tree, we have to decrement the count of the respective fruits

        When we have picked two types of fruits, update the maximum number of fruits we have taken if the current number of fruits we have taken is greater than the maximum.

        return the maximum fruits we can pick CONSECUTIVELY
        '''
        #
        fruitsInBasket = dict()
        maximumNumberOfFruitsPicked = 0

        #pointers for the begin and last tree from which the fruits are picked
        begin, end = 0, 0
        
        while end < len(fruits):
            currentFruit = fruits[end]
            if currentFruit in fruitsInBasket:
                fruitsInBasket[currentFruit] += 1
            else:
                fruitsInBasket[currentFruit] = 1
            
            end += 1

            while len(fruitsInBasket) > 2:
                beginFruit = fruits[begin]
                fruitsInBasket[beginFruit] -= 1
                if fruitsInBasket[beginFruit] == 0:
                    del fruitsInBasket[beginFruit]
                begin += 1

            if len(fruitsInBasket) == 2:
                currentFruitsPicked = 0
                for value in fruitsInBasket.values():
                    currentFruitsPicked += value
                if maximumNumberOfFruitsPicked < currentFruitsPicked:
                    maximumNumberOfFruitsPicked = currentFruitsPicked
            
        return maximumNumberOfFruitsPicked