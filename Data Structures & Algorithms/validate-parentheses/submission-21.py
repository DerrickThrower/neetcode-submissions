class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        valid = { ")": "(",
        "}": "{",
        "]": "["
        }


        for char in s:
            if char in valid:

                if stack and stack[-1] == valid[char]:
                    stack.pop()

                else:
                    return False


            
            else:

                stack.append(char)


        if not stack:
            return True

        return False

        