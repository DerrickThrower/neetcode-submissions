class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closing = {
            "}":"{",
            "]":"[",
            ")":"("
        }


        for char in s:

            if char in closing:

                if stack and stack[-1] == closing[char]:
                    stack.pop()
                else:
                    return False
    
            else:
                stack.append(char)


        if stack:
            return False

        return True





        
        