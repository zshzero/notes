# Double Linked List Interview LeetCode Exercises

### [1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list)
```py
# BruteForce
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(1)
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # check if DLL has no or only one node
    if not head or not head.next:
        return head

    # calculate length
    count = 0
    itr = head
    while itr:
        count += 1
        itr = itr.next
    
    # traverse until end to match left and right nodes
    left, right = head, head
    i = 0
    itr = head
    while itr:
        if i == k-1:     
            left = itr
        if i == count - k:
            right = itr
        i += 1
        itr = itr.next

    # swap values
    temp = right.val
    right.val = left.val
    left.val = temp
    return head
```

```py
# Two pointer
# Time Complexity - O(k + (n - k)) => O(n)
# Space Complexity - O(1)
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # check if DLL has no or only one node
    if not head or not head.next:
        return head

    # initialize slow, head as head
    slow = head
    fast = head
    i = 1
    # move fast till it reaches left node
    while i < k:
        i += 1
        fast = fast.next
    left = fast

    # move slow, fast till fast reaches last node
    while fast.next:
        fast = fast.next
        slow = slow.next
    # Now, slow has reached right node
    right = slow

    # swap values
    left.val, right.val = right.val, left.val
    return head
```

### [0. Reverse Double Linked List]()
```py
# BruteForce
# Time Complexity - O(n)
# Space Complexity - O(1)
def reverse(self) -> Optional[ListNode]:
    current_node = self.head
    # traverse until end
    while current_node:
        # swap pointers
        current_node.prev, current_node.next = current_node.next, current_node.prev
        # move to prev as its swapped
        current_node = current_node.prev
    # swap head and tail
    self.head, self.tail = self.tail, self.head
```

### [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list)
```py
# BruteForce on SLL
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(n)
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # initialize stack
    s = []
    top = -1

    # add all elements to stack
    itr = head 
    while itr:
        s.append(itr.val)
        itr = itr.next
        top += 1
    print(s, top)

    # traverse LL and compare its value with top ele
    itr = head
    while itr:
        print(itr.val,s[top])
        if itr.val != s[top]:
            return False
        itr = itr.next
        top -= 1
    
    return True
```

```py
# Two pointer and Reverse on SLL
# Time Complexity - O(n/2 + n/2 + n/2) => O(n)
# Space Complexity - O(1)
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # its palindrome if LL has no or one node
    if not head or not head.next: return True

    # initialize slow, head as head and find middle node
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse 1st half of LL
    back = None
    while slow:
        front = slow.next
        slow.next = back
        back = slow
        slow = front

    # start comparing from either end of LL
    left, right = head, back
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True
```

```py
# Two pointer on DLL
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(n)
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # its palindrome if LL has no or one node
    if not self.head or not self.head.next:
        return True
    
    # find middle (length // 2)
    slow, fast = self.head, self.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        # print("-",slow.value)
        
     # traverse till middle
    left, right = self.head, self.tail
    while left is not slow.next:
        # compare values from either side
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev
    return True
```

### [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)
```py
# Two pointer on SLL (By modifying node values)
# Time Complexity - O(n)
# Space Complexity - O(1)
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # nothing to swap if LL has no or one node
    if not head or not head.next:
        return head

    # initialize left and pointer as adjacent nodes
    left, right = head, head.next
    # traverse until even no. of nodes present to swap
    while left and left.next:
        left.val, right.val = right.val, left.val
        # check if there are 2 nodes ahead to swap
        if not right or not right.next:
            break 
        left = left.next.next
        right = right.next.next
        print(left, right)
    return head
```

```py
# Two pointer on SLL (By modifying nodes)
# Time Complexity - O(n)
# Space Complexity - O(1)
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # nothing to swap if LL has no or one node
    if not head or not head.next:
        return head

    # add dummy node to avoid edge cases
    dummy = ListNode(0, head)
    # initialize prev and curr nodes
    prev, curr = dummy, head
    
    # traverse till until last pair of nodes
    while curr and curr.next:
        # save initial node of nextPair
        nextPair = curr.next.next
        
        # swap pointers
        second = curr.next
        curr.next = nextPair
        second.next = curr
        prev.next = second

         # update pointers for next pair
        prev = curr 
        curr = nextPair
                    
    return dummy.next

# Two pointer on DLL (By modifying nodes)
# Time Complexity - O(n)
# Space Complexity - O(1)
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # nothing to swap if LL has no or one node
    if not head or not head.next:
        return head

    # add dummy node to avoid edge cases
    dummy = ListNode(0, head)
    # initialize prev and curr nodes
    prev, curr = dummy, head
    
    # traverse till until last pair of nodes
    while curr and curr.next:
        # save initial node of nextPair
        nextPair = curr.next.next
        
        # swap pointers
        second = curr.next
        curr.prev, curr.next = second, nextPair
        second.prev, second.next = prev, curr
        prev.next = second # setting prev.prev isn't required as its
                          # its already pointing at right prev node

         # update pointers for next pair
        prev = curr 
        curr = nextPair
                    
    return dummy.next
```