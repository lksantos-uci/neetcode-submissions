class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreq, tFreq = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sFreq[s[i]] += 1 
            tFreq[t[i]] += 1 
        for c in sFreq:
            if sFreq[c] != tFreq[c]:
                return False
        return True
