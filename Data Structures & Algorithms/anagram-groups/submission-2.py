class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        res = []
        for ele in strs:
          arr = [0] * 26
          for s in ele:
            arr[ord(s) - ord('a')] += 1
          t = tuple(arr)
          if t not in freq:
            freq[t] = [ele]
          else:
            freq[t].append(ele)
        return list(freq.values())