# Linked List Interview  LeetCode Exercises

### [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)

```py
# BruteForce
# Time Complexity - O(n + n/2) => O(n)
# Space Complexity - O(1)
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # traverse LL to find the length
    itr = head
    length = 0
    while itr:
        itr = itr.next
        length += 1
    print(length)

    # calculate mid
    mid = (length//2) + 1 
    print(mid)

    # traverse again to the middle of the LL
    itr = head
    i = 1
    while i < mid:
        itr = itr.next
        i += 1

    # return middle node
    return itr
```

```py
# Two pointer or Floyd's Tortoise & Hare algo 
# Time Complexity - O(n/2) => O(n)
# Space Complexity - O(1)
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # initialize slow and faster ptr with head
    slowPtr, fastPtr = head, head

    # traverse LL until fast ptr reaches the end
    # 1st condition is when LL is of even length
    # 2nd condition is when LL is of odd length
    while fastPtr and fastPtr.next:
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

    # return slow ptr which is at the mid
    return slowPtr
```

### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)

```py
# BruteForce 
# Time Complexity - O(n*2*[Time Complexity of add and check of element in set])
# Space Complexity - O(n)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    h = set()
    itr = head
    
    # traverse LL and add the nodes to the set
    while itr:
        # until it tries to add dup node
        if itr in h:
            return True
        h.add(itr)
        itr = itr.next
    return False
```

```py
# Two pointer or Floyd's Tortoise & Hare algo 
# Time Complexity - b*O(n) (b here is the no. of cycle it took for them to meet) => O(n) 
# Space Complexity - O(1)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # initialize slow and faster ptr with head
    slowPtr, fastPtr = head, head

    # traverse LL until end
    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr is fastPtr:
            return True
    return False
```

### [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

```py
# BruteForce 
# Time complexity: O(Length)+O(Length - N) => O(N)
# Space complexity: O(1)
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # find the length LN
    itr = head
    length = 0
    while itr:
        itr = itr.next
        length += 1
    print("length", length)

    # when condition wants to remove head
    if length == n:
        head = head.next
        return head

    # calculate index of Previous Node to that of removal
    previousNodeToThatOfRemove = length - n
    print("previousNodeToThatOfRemove", previousNodeToThatOfRemove)

    # traverse to the Previous Node to that of removal
    i = 1
    itr = head
    while(i < previousNodeToThatOfRemove):
        itr = itr.next
        i += 1
    print("previousNode", itr.val)

    # remove the nth node
    delNode = itr.next
    itr.next = delNode.next
    delNode = None

    return head
```

```py
# Two pointer or Floyd's Tortoise & Hare algo 
# Time Complexity - O(GapTraversal) + O(N - GapTraversal) => O(n) 
# Space Complexity - O(1)
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # remove zero or one node
    if not head or not head.next:
        return None

    # initialize slow and faster ptr with head
    slowPtr, fastPtr = head, head

    # move fastPtr n steps
    for _ in range(n):
        # When N equals length and wants to remove head
        if not fastPtr.next:
            return head.next
        fastPtr = fastPtr.next

    # move slowPtr and fastPtr till end
    while fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next

    # Remove the nth node
    delNode = slowPtr.next
    slowPtr.next = delNode.next
    delNode = None

    return head
```

### [86. Partition List](https://leetcode.com/problems/partition-list)

```py
# Partition by comparing values 
# Time complexity: O(N)
# Space complexity: O(1)
def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    itr = head
    # create two new LL and its tail
    p1Itr, p2Itr = ListNode(), ListNode()
    p1Tail, p2Tail = p1Itr, p2Itr

    # traverse until end of LL
    while itr:
        # check and point the node to resp. LL by checking its value
        if(itr.val < x):
            p1Itr.next = itr
            p1Itr = p1Itr.next
        else:
            p2Itr.next = itr
            p2Itr = p2Itr.next
        itr = itr.next

    print(p2Tail)
    print(p1Tail)
    # check if partition 1 is empty and remove initial dummyNode
    if p1Tail.next:
        p1Tail = p1Tail.next
        p2Itr.next = None
    else:
        p2Tail = p2Tail.next
        return p2Tail
    # stitch the partitions and return partition 1 head
    p1Itr.next = p2Tail.next
    p2Itr = None
    return p1Tail
```
[83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list)

```py
# BruteForce on unsorted List 
# Time complexity: O(N^2)
# Space complexity: O(1)
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    itr1 = head
    # traverse LL till end
    while itr1:
        itr2 = itr1
        # traverse LL till last node
        while itr2.next:
            #  remove itr2 if next node is same val as current else incr
            if itr1.val == itr2.next.val:
                itr2.next = itr2.next.next
            else:
                itr2 = itr2.next   
        # incr itr1
        itr1 = itr1.next
            
    return head
```

```py
# Using Set on unsorted List 
# Time complexity: O(N)
# Space complexity: O(N)
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
   # create set and have to node, previous and current iterator
    s = set()
    prev = None
    itr = head
    # traverse LL till end
    while itr:
        # remove itr if the val exist in set else add and incr
        if itr.val in s:
            prev.next = itr.next
        else:
            s.add(itr.val)
            prev = itr
        itr = itr.next

    return head
```

```py
# Two Pointer on sorted List 
# Time complexity: O(N)
# Space complexity: O(1)
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # check if LL has more than 1 nodes
    if not head or not head.next:
        return head
        
    # initialize current ptr with head
    curr = head
    # traverse LL till last node
    while curr and curr.next:
        # check if current and next node(adjacent nodes) have same value else incr
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
```

[1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

```py
# BruteForce
# Time complexity: O(N + N) => O(N)
# Space complexity: O(N)
def getDecimalValue(self, head: Optional[ListNode]) -> int:
    l = []
    # convert LL to list 
    while head:
        l.append(head.val)
        head = head.next

    s = 0
    count = len(l)
    print(l, count)
    # traverse List and add val raised to power 2 if val is 1 
    i = 0
    while i < count:
        print(i, l[i], pow(2, count-1-i))
        if l[i] == 1:
            s += pow(2, count-1-i)
        i += 1
    return s
```

```py
# Bit Shifting
# Time complexity: O(N)
# Space complexity: O(1)

# Example Logic for 110 = 13:
# 0 * 2 # 
# 0 + 1 # add it wil bit

# 1 * 2 # Multiply sum by 2
# 2 + 1 # add it wil bit

# 3 * 2 # Multiply sum by 2
# 6 + 0 # add it wil bit

# 6 # Answer
def getDecimalValue(self, head: Optional[ListNode]) -> int:
    s = 0
    while head:
        # Multiply sum by 2
        s = s * 2
        # add bit
        s += head.val
        head = head.next
    return s
```

[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)
```py
# 3 pointer
# Time complexity: O(N)
# Space complexity: O(1)
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # when no elements
    if not head: return None
    # when 1 elements
    if not head.next: return head
    # when 2 elements
    if not head.next.next:
        tail = head.next
        tail.next = head
        head.next = None
        head = tail
        return head
    
    # initial 3 pointers as curr, back and front
    front = head.next
    curr = head
    back = None
    # traverse until last node and point LL in reverse direction
    while curr.next:
        curr.next = back
        back = curr
        curr = front
        front = front.next
    # point last node to rest of LL
    curr.next = back
    head = curr
    return head
```

```py
# 3 pointer with dummy Node to avoid edge cases
# Time complexity: O(N)
# Space complexity: O(1)
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    curr = head
    back = None
    # traverse until end and point LL in reverse direction
    while curr:
        # temp store of next node
        front = curr.next
        curr.next = back
        back = curr
        curr = front
    return back
```

[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii)
```py
# 4 pointer with dummy Node to avoid edge cases
# Time complexity: O(N)
# Space complexity: O(1)
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
    dummy =  ListNode(0,head)   

    # traverse until left position
    prevLeft = dummy
    curr = head
    i = 0
    while i < left-1:  
        prevLeft = curr
        curr = curr.next
        i += 1

    # traverse and reverse until right position
    i = 0
    back = None
    while i < right-left+1:
        front = curr.next
        curr.next = back
        back = curr
        curr = front
        i += 1

    # Update pointers of right and left position nodes 
    prevLeft.next.next = curr
    prevLeft.next = back
    return dummy.next
```