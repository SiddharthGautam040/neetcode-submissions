class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        time = []
        for i in range(len(cars)):
            time.append((target - cars[i][0]) / cars[i][1])
            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()
        
        return len(time)