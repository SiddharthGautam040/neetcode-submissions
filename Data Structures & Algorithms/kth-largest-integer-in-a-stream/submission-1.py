class MinHeap:
    def __init__(self, heap=[]):
        self.heap = heap
        self.heapify()

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i] >= self.heap[parent]:
                break

            self.heap[parent], self.heap[i] = (
                self.heap[i],
                self.heap[parent]
            )

            i = parent

    def pop(self):
        if not self.heap:
            return 
        n = len(self.heap) - 1
        smallest = self.heap[0]
        self.heap[n], self.heap[0] = self.heap[0], self.heap[n]
        self.heap.pop()
        self.shift_down()
        return smallest


    def shift_down(self, parent=0):
        n = len(self.heap) - 1
        if not self.heap: return None

        while True:
            child1 = 2 * parent + 1
            child2 = 2 * parent + 2

            if child1 <= n and child2 <= n:
                smaller_child = (
                    child1 if self.heap[child1] < self.heap[child2]
                    else child2
                )
            elif child1 <= n:
                smaller_child = child1
            else:
                break

            if self.heap[smaller_child] >= self.heap[parent]:
                break

            self.heap[parent], self.heap[smaller_child] = (
                self.heap[smaller_child],
                self.heap[parent]
            )

            parent = smaller_child

    def heapify(self):
        n = len(self.heap)
        for i in range((n//2) - 1, -1, -1):
            self.shift_down(i)

    def peek(self):
        return self.heap[0]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = MinHeap(nums)

        while len(self.heap.heap) > k:
            self.heap.pop()

    def add(self, val: int) -> int:
        if len(self.heap.heap) < self.k:
            self.heap.push(val)

        elif val > self.heap.peek():
            self.heap.pop()
            self.heap.push(val)

        return self.heap.peek()
