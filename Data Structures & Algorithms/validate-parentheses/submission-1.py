class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        bracs = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        for i in s:
            if i in bracs.keys():
                if len(arr) == 0:
                    return False
                else:
                    ele = arr.pop()
                    if ele != bracs[i]:
                        return False
            else:
                arr.append(i)
        return True if len(arr) == 0 else False