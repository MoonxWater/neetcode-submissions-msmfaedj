class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer, back_pointer = 0, len(s) - 1

        for i in range(len(s)//2 + 1):
            if not(s[pointer].isalnum()):
                pointer += 1
                continue
            elif not(s[back_pointer].isalnum()):
                back_pointer -= 1
                continue
            elif s[pointer].lower() != s[back_pointer].lower():
                return False
            
            pointer += 1
            back_pointer -= 1

        return True 
                