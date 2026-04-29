class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        stack = []
        for i in range(len(cars)):
            t = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append(t)
            else:
                if t > stack[-1]:
                    stack.append(t)
        return len(stack)