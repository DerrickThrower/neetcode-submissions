class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p,s) for p,s in zip(position, speed)]# pair cars pos and speed

        pair.sort(reverse=True) #reverse the order to closest to target to 
        stack = []

        for p,s in pair:
            # Calculate how long this car takes to reach the target
            # formula = distance / speed
            # distance left = target - position
            stack.append((target-p)/s)
            # If there are at least 2 cars/fleets
            # and the current car reaches the target
            # faster or at the same time as the fleet in front,
            # then it catches up and becomes part of that fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)