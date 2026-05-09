class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(','}':'{',']':'['}

        for c in s:#iterate through list
            if c in closeToOpen:#if c is a closing parenthesis
                if stack and stack[-1] == closeToOpen[c]:#if the stack and the one before it is a valid parenthesis 
                    stack.pop()#remove it from the stack
                else:
                    return False#if it isnt then return false 

            else:
                stack.append(c)#if its open or not a bracket then append to stack

        return True if not stack else False#if stack is empty then its a valid parenthessi
        