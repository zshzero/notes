#  Basic Sort LeetCode Exercises

### [Bubble Sort Linked List](https://leetcode.com/problems/insertion-sort-list)

```py
# Bubble Sort
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def bubbleSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # return if LL has 0 or 1 node
    if not head or not head.next: 
        return head

    # var to indicate till where its sorted
    sorted_until = None
    # loop only unsorted section
    while sorted_until != head.next:
        # itr to compare adj node
        curr = head
        # loop from head to unsorted section
        while curr.next != sorted_until:
            front = curr.next
            # swap if front is greater than curr
            if curr.val > front.val:
                curr.val, front.val = front.val, curr.val
            curr = curr.next
        # Highest node is bubbled at end. update var after each itr
        sorted_until = curr
    return head
```

### [Selection Sort Linked List](https://leetcode.com/problems/insertion-sort-list)

```py
# Selection Sort
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def selectionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # return if LL has 0 or 1 node
    if not head or not head.next: 
        return head

    # itr till last but one node
    i = head
    while i.next:
        # assume 1st node is min
        min_value = i
        # itr from i's next till end 
        j = i.next
        while j:
            # update min value if you find new one
            if min_value.val > j.val:
                min_value = j
            j = j.next
        # swap min value with curr
        i.val, min_value.val = min_value.val, i.val
        i = i.next
    return head
```

### [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list)

```py
# Insertion Sort - Value Swap
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # return if LL has 0 or 1 node
    if not head or not head.next: 
        return head

    # create 2 var i and prev to itr
    i = head.next
    prev = head
    while i:
        # only try to sort when last ele of sorted section 
        # is greater than curr
        if prev.val > i.val:
            # itr sorted section
            j = head
            while j != i:
                # swap values when ele from sorted section 
                # is greater than curr
                if j.val > i.val:
                    j.val, i.val = i.val, j.val
                j = j.next
        i = i.next
        prev = prev.next
    return head
```

```py
# Insertion Sort - Node Swap
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # return if LL has 0 or 1 node
    if not head or not head.next: 
        return head

    # create dummy node before head to avoid edge cases
    dummy = ListNode(-5001, head)
    # initialize variable to itr 
    i = head.next
    ip = head
    
    while i:
        # only try to sort when last ele of sorted section 
        # is greater than curr
        if i.val >= ip.val:
            ip = i
            i = i.next
            continue
        
        # itr till curr to find insert pos
        j = dummy
        while j.next.val < i.val:
            j = j.next

        # swap nodes
        ip.next = i.next
        i.next = j.next
        j.next = i
        # update curr
        i = ip.next

    return dummy.next
```

### [75. Sort Colors](https://leetcode.com/problems/sort-colors)

```py
# Dict
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(n)
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # initialize dict to keep track of count
    d = {}
    # traverse nums and update dict
    for num in nums:
        if num in d: d[num] += 1
        else: d[num] = 1

    # create var index to track entire nums
    i = 0
    # loop each key from dict
    for key in [0,1,2]:
        # check if key is present in dict
        if key not in d: continue
        # itr till key's val and update nums val
        for _ in range(d[key]):
            nums[i] = key
            i += 1
```
