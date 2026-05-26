class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in brackets.keys():
                if not stack or stack[-1] != brackets[c]:
                    return False
                
                stack.pop()
            else:
                stack.append(c)
        
        return not stack

        