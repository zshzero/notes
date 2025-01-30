#  Tree Traversal LeetCode Exercises

### [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)

```py
# DFS InOrder
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(n(list) + n(recursion stack)) => O(n)
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # initialize result to store resultant after traversing
    result = []
    
    #recursive func to traverse bst
    def traverse_dfs_inorder(node):
        if not node: return
        if node.left: traverse_dfs_inorder(node.left)
        # append value after you see left subtree
        result.append(node.val)
        if node.right: traverse_dfs_inorder(node.right)

    traverse_dfs_inorder(root)

    # edge case when bst has only one node
    if len(result) == 1: return True
    
    # compare ele and see if they are in asc order
    for i in range(len(result)-1):
        if result[i] >= result[i+1]:
            return False
    return True
```

```py
# DFS
# Time Complexity - O(n)
# Space Complexity - O(n)
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # recursive func to check if node val exist between left and right subtrees
    def traverse_dfs_inorder(node, l, r):
        # base case
        if not node:
            return True
        # check if node val exist between left and right boundary
        if not (l < node.val and node.val < r):
            return False

        # traverse to left and right nodes with their resp. new boundaries
        return (traverse_dfs_inorder(node.left, l, node.val) and
        traverse_dfs_inorder(node.right, node.val, r))

    # initialize call with root, min and max
    return traverse_dfs_inorder(root, -inf, inf)
```

### [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

```py
# DFS InOrder
# Time Complexity - O(n)
# Space Complexity - O(n(list) + n(recursion stack)) => O(n)
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # initialize result to store resultant after traversing
    result = []

    #recursive func to traverse bst
    def traverse_dfs_inorder(node):
        if not node: return
        if node.left: traverse_dfs_inorder(node.left)
        result.append(node.val)
        if node.right: traverse_dfs_inorder(node.right)
    
    traverse_dfs_inorder(root)
    # return kth ele from sorted list
    return result[k-1]
```

```py
# DFS InOrder without List
# Time Complexity - O(n)
# Space Complexity - O(n)
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # variable to store kth ele
    result = 0
    def traverse_dfs_inorder(node):
        # base case
        if not node: return
        # traverse left
        if node.left: traverse_dfs_inorder(node.left)
        # get k in scope and reduce 1 left node is processed
        nonlocal k
        k -= 1 
        # store val once it reaches kth ele
        if k == 0: 
            nonlocal result
            result = node.val
            return
        # traverse right
        if node.right: traverse_dfs_inorder(node.right)
    
    traverse_dfs_inorder(root)
    return result
```