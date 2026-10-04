class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {'}': '{', ')': '(', ']': '['}

        for let in s:
            if let in closeOpen:
                if stack and stack[-1] == closeOpen[let]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(let)
        
        if not stack:
            return True
        else:
            return False
    


'''
{([{}])}


'''
        