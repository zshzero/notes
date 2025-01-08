#  Merge Sort LeetCode Exercises

### [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)

```py
# Merge
# Time Complexity - O(n + m)
# Space Complexity - O(1)
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # initialize dummy node before head to avoid edge cases
    dummy = ListNode(-101)

    # initialize itr for 3 LLs
    itr = dummy
    itr1 = list1
    itr2 = list2
    
    # compare val if both LL has nodes
    while itr1 and itr2:
        # add least valued node to itr
        if itr1.val < itr2.val:
            itr.next = itr1
            itr1 = itr1.next
        else:
            itr.next = itr2
            itr2 = itr2.next
        itr = itr.next

    # add remaining nodes to itr when itr2 is done
    while itr1:
        itr.next = itr1
        itr = itr.next
        itr1 = itr1.next

    # add remaining nodes to itr when itr1 is done
    while itr2:
        itr.next = itr2
        itr = itr.next
        itr2 = itr2.next

    return dummy.next
```
