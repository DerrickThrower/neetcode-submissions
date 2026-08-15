from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        q = deque(students)
        stack = deque(sandwiches)
        count = 0

        while q and count < len(q):

            if q[0] == stack[0]:
                q.popleft()
                stack.popleft()
                count = 0

            else:
                q.append(q.popleft())
                count +=1

        return len(q)