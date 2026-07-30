class Solution:
    
    def isValid(self, s: str) -> bool:
        brackets = {'{':'}', '[':']', '(':')'}
        stack = []

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            
            elif char in brackets.values():
                if stack and char == brackets[stack[-1]]:
                    stack.pop()

                else:
                    return False

        return True if not stack else False