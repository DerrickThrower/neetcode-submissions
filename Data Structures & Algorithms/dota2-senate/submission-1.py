from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s = deque()
        d = deque()

        for i,side in enumerate(senate):
            if side == "R":
                s.append(i)
            else:
                d.append(i)

    
        while s and d:
            r = s.popleft()
            e = d.popleft()

            if r < e:
                s.append(r+n)

            else:
                d.append(e+n)

        return "Radiant" if s else "Dire"
        