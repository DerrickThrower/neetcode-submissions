"""Tree traversal pattern utilities.

Tree traversal patterns are duplicated across:
  - depth-of-binary-tree (BFS with deque, iterative DFS)
  - binary-tree-diameter (DFS height calculation)
  - invert-a-binary-tree (4 submissions, recursive swap)
  - same-binary-tree (2 submissions, recursive comparison)
  - subtree-of-a-binary-tree (nested DFS)
  - valid-binary-search-tree (DFS with bounds)
  - lowest-common-ancestor-in-binary-search-tree (BST traversal)
  - kth-smallest-integer-in-bst (inorder traversal)
  - level-order-traversal-of-binary-tree (BFS)
"""

from collections import deque
from typing import Callable, List, Optional

from shared.data_structures import TreeNode


def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """Max depth using BFS (level-order traversal).

    Extracted from depth-of-binary-tree/submission-0.py.
    """
    if not root:
        return 0

    level = 0
    q = deque([root])

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

    return level


def max_depth_dfs(root: Optional[TreeNode]) -> int:
    """Max depth using iterative DFS with stack.

    Extracted from depth-of-binary-tree/submission-1.py.
    """
    if not root:
        return 0

    stack = [[root, 1]]
    res = 1

    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res


def diameter(root: Optional[TreeNode]) -> int:
    """Binary tree diameter (longest path between any two nodes).

    Extracted from binary-tree-diameter/submission-0.py.
    """
    result = 0

    def dfs(curr: Optional[TreeNode]) -> int:
        nonlocal result
        if not curr:
            return 0
        left = dfs(curr.left)
        right = dfs(curr.right)
        result = max(result, left + right)
        return 1 + max(left, right)

    dfs(root)
    return result


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree (mirror).

    Extracted from invert-a-binary-tree submissions 1-4, all performing:
        root.left, root.right = root.right, root.left
        invert(root.left)
        invert(root.right)
    """
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Check if two trees are structurally identical.

    Extracted from same-binary-tree submissions 0-1:
        if not p and not q: return True
        if p and q and p.val == q.val:
            return same(p.left, q.left) and same(p.right, q.right)
        return False
    """
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return False


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Validate a binary search tree using DFS with bounds.

    Extracted from valid-binary-search-tree/submission-0.py.
    """

    def validate(
        node: Optional[TreeNode], left: float, right: float
    ) -> bool:
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return validate(node.left, left, node.val) and validate(
            node.right, node.val, right
        )

    return validate(root, float("-inf"), float("inf"))


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Level-order (BFS) traversal returning values grouped by level.

    Extracted from level-order-traversal-of-binary-tree/submission-0.py.
    """
    if not root:
        return []

    queue = deque([root])
    res: List[List[int]] = []

    while queue:
        level_list = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_list)

    return res


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Inorder traversal (left, root, right) — useful for BST problems.

    Pattern used in kth-smallest-integer-in-bst/submission-0.py.
    """
    result: List[int] = []

    def inorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result
