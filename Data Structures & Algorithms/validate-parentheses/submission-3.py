class Solution:
    def isValid(self, s: str) -> bool:
        inverse = {
            '{':'}',
            '[':']',
            '(':')'
        }
        arr = []
        for b in s:
            if b in inverse.keys():
                arr.append(b)
            elif arr:
                val = arr.pop()
                if inverse[val] != b:
                    return False
            else:
                return False
        return len(arr) == 0
