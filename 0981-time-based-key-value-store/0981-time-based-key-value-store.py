class TimeMap(object):

    def __init__(self):
        self.store  = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res, values = "", self.store.get(key,[])
        l, r = 0, len(values)-1
        while l <= r:
            mid = l+(r-l)//2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                res = values[mid][1]
                l = mid + 1
        return res
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)