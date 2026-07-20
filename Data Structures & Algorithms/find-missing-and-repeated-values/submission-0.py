class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        seen = {}
        a = None
        b = None
        for n in grid:
            for m in n:
                if m in seen:
                    a = m

                else:
                    seen[m] = None


        for n in range(1, len(grid)*len(grid)+1):
            if n not in seen:
                b = n


        return [a,b]        