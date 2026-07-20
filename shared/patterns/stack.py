"""Stack-based pattern utilities.

Stack patterns are duplicated across:
  - validate-parentheses (6 submissions with identical logic)
  - daily-temperatures
  - evaluate-reverse-polish-notation (4 submissions)
  - car-fleet

Common structure:
    stack = []
    for item in items:
        while stack and condition:
            stack.pop()
        stack.append(item)
"""

from typing import Dict, List


def is_valid_parentheses(s: str) -> bool:
    """Validate that brackets are properly matched and nested.

    Extracted from validate-parentheses submissions 1, 15, 20, 21 — all using:
        stack = []
        close_to_open = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else: return False
            else: stack.append(c)
        return not stack
    """
    stack: List[str] = []
    close_to_open: Dict[str, str] = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return not stack


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """Days until a warmer temperature using a monotonic stack.

    Extracted from daily-temperatures/submission-0.py.
    """
    res = [0] * len(temperatures)
    stack: List[List[int]] = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, stack_idx = stack.pop()
            res[stack_idx] = i - stack_idx
        stack.append([t, i])

    return res


def eval_rpn(tokens: List[str]) -> int:
    """Evaluate Reverse Polish Notation expression.

    Extracted from evaluate-reverse-polish-notation submissions 0, 4, 5, 6.
    """
    stack: List[int] = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b) / a))
        else:
            stack.append(int(c))

    return stack[0]
