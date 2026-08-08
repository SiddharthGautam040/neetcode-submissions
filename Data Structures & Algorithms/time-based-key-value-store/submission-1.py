class TimeMap:

    def __init__(self):
        self.lookup = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.lookup.get(key, list())
        arr.append((int(timestamp), value))
        self.lookup[key] = arr
        return None


    def get(self, key: str, timestamp: int) -> str:
        arr = self.lookup.get(key)
        if not arr:
            return ""
        index = self.binary_search(arr, int(timestamp))
        if index == -1:
            return ""
        return arr[index][1]


    def binary_search(self, arr, key):
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = l + ((r-l) // 2)

            if arr[mid][0] == key:
                return mid
            elif arr[mid][0] < key:
                l = mid + 1
            else:
                r = mid - 1
        return r
