class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        ends = {
            
            "}":"{",
            ")":"(",
            "]":"[",
        }

        for char in s:

            if char in ends:
                
            
                if stack and ends[char] == stack[-1]:

                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        if not stack:
            return True
        
        return False