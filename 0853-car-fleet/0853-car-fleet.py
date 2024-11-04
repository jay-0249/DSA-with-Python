class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Pair each car's position with its speed and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, spd in cars:
            # Calculate time for this car to reach the target without handling zero speed
            time = float(target - pos) / spd
            
            # If the stack is empty or the current car takes longer than the last car in stack
            if not stack or time > stack[-1]:
                stack.append(time)
        
        # The number of elements in the stack represents the number of fleets
        return len(stack)
        