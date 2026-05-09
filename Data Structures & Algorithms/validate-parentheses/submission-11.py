class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        opening = {"(","{","["}


        for char in s:
            if char in opening:
                stack.append(char)

            if len(stack) != 0:
                if char == "]":
                    if stack[-1] == "[":
                        stack.pop(-1)
                    else:
                        return False

                if char == "}":
                    if stack[-1] == "{":
                        stack.pop(-1)

                    else:
                        return False

              

                if char == ")":
                    if stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        return False

            
            else:
                return False



        
        if len(stack) > 0:
            return False
        return True






        
        