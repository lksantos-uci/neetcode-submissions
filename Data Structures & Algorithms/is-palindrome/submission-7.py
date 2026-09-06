class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = s.upper()
        low, high = 0, len(newS) - 1
        while (low <= high):
            while (low <= high) and not newS[low].isalnum():
                low += 1
            while (low <= high) and not newS[high].isalnum():
                high -= 1
            if (low <= high):
                if newS[low] == newS[high]:
                    low += 1
                    high -= 1
                else:
                    return False
        return True
                
