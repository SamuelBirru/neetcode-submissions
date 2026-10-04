class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for words in s:
            if words.isalnum():
                word += words.lower()

        l = 0
        r = len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True