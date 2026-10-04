class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ""
        for word in s:
            if word.isalnum():
                words += word.lower()
        
        front = 0
        back = len(words) - 1

        while front < back:
            if words[front] != words[back]:
                return False
            front += 1
            back -= 1
        
        return True