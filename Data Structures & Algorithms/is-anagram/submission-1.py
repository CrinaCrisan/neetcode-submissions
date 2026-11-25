class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frs = [0]*26
        frt = [0]*26
        for i in s:
            j = ord(i) - ord('a')
            frs[j] += 1
        for i in t:
            j = ord(i) - ord('a')
            frt[j] += 1
        for i in range (0, 26):
            if frs[i] != frt[i]:
                return False
        return True
        