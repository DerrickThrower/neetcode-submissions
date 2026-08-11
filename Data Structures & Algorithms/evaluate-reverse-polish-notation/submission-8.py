class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []
        res = 0
        for t in tokens:

            if t == "+":
                y = s.pop()
                x = s.pop()

                s.append(x+y)

            elif t == "-":
                y = s.pop()
                x = s.pop()

                s.append(x-y)
            
            elif t == "*":
                y = int(s.pop())
                x = int(s.pop())

                s.append(x*y)

            elif t == "/":
                y = s.pop()
                x = s.pop()

                s.append(int(float(x)/y))

            else:
                s.append(int(t))
            

        return s.pop()

        