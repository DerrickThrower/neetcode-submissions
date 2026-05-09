class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        s = []

        for n in tokens:

            if n == "+":
                val1 = int(s.pop(-1))
                val2 = int(s.pop(-1))

                s.append(val1 + val2)
            elif n == "-":
                val1 = int(s.pop(-1))
                val2 = int(s.pop(-1))

                s.append(val2 - val1)
            elif n == "/":
                val1 = int(s.pop(-1))
                val2 = int(s.pop(-1))

                s.append(val2 / val1)
            elif n == "*":
                val1 = int(s.pop(-1))
                val2 = int(s.pop(-1))

                s.append(val1 * val2)
            else:

                s.append(n)

        return int(s.pop(-1))

                

        