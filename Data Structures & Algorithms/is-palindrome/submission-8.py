class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make string all caps
        word = []
        for c in s:
            word.append(c.upper())
        # Check if it is a palindrome
        low, high = 0, len(word) - 1
        while low <= high:
            while low <= high and not word[low].isalnum():
                low += 1
            while low <= high and not word[high].isalnum():
                high -= 1
            if low <= high:
                if word[low] == word[high]:
                    low += 1
                    high -= 1
                else:
                    return False
        return True