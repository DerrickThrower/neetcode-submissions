class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []

        for char in operations:

            if char == "+":
                var1 = record[-1]
                var2 = record[-2]
                record.append(var1 + var2)

            elif char == "D":
                record.append(record[-1]*2)

            elif char == "C":
                record.pop()

            
            else:
                record.append(int(char))

        return sum(record)