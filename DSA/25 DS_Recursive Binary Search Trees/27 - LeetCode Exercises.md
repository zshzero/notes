# Recursive BST LeetCode Exercises

### [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)

```py
# Recursion
# Time Complexity - O(n)
# Space Complexity - O(n)(node creation) + O(log n)(recursion stack)
#   Height of balanced tree is O(log n) and unbalanced tree is O(n)(worst-case)
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    # recursive method to add ele at mid to tree
    def r_insert(l,r):
        # base case: return if left is less than right
        if l > r: 
            return None
        # calculate mid and get its node
        mid = (l + r) // 2
        node = TreeNode(nums[mid])
        # recursively insert from left array to create left substree
        node.left = r_insert(l, mid-1)
        # recursively insert from right array to create right substree
        node.right = r_insert(mid+1, r)
        # return node to assign it to tree's left/right
        return node
    
    return r_insert(0,len(nums) - 1)
```

### [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree)

```py
# Recursion
# Time Complexity - O(n)
# Space Complexity - O(n)(node creation) + O(log n)(recursion stack)
def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    def r_insert(node):
        if not node: return None
        if not node.next: return TreeNode(node.val)

        left, right, left_prev = node, node, None
        while right and right.next:
            left_prev = left
            left = left.next
            right = right.next.next
        
        tree_node = TreeNode(left.val)
        left_prev.next = None
        tree_node.left = r_insert(node)
        tree_node.right = r_insert(left.next)
        return tree_node
    
    return r_insert(head)
```

### [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree)

```py
# Recursion
# Time Complexity - O(n)
# Space Complexity - O(n) for skewed tree and O(log n) for balanced tree (recursion stack)
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # recursive method to swap nodes
    def swap_nodes(node):
        # base case: return if node is None
        if not node:
            return None
        
        # recursively swap left and right nodes
        node.left, node.right  = swap_nodes(node.right), swap_nodes(node.left)
        # return node with children swapped
        return node

    return swap_nodes(root)
```