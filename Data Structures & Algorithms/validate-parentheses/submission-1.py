class Solution:
    
    def isValid(self, s: str) -> bool:
        brackets = {'{':'}', '[':']', '(':')'}
        openbrackets = {'{', '[', '('}
        closebrackets = {'}', ']', ')'}
        stack = []

        for char in s:
            if char in openbrackets:
                stack.append(char)
            
            elif char in closebrackets:
                if stack and char == brackets[stack[-1]]:
                    stack.pop()

                else:
                    return False

        if not stack:
            return True

        else: 
            return False
            
            



        