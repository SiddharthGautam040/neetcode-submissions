class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[i, j] for i,j in zip(position, speed)]
        stack = []
        fleet = 0

        pairs.sort(reverse=True)

        for pos, s in pairs:
            time = (target - pos) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
