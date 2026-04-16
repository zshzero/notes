# Remove the Kth Last Node From a Linked List

Return the head of a singly linked list after removing the kth node from the end of it.

#### Example:

![The image represents a linked list data structure illustrating the concept of finding the k<sup>th</sup> to last element](./images/bfcc9f49_remove-kth-last-node-ZMDYO4KR.svg)

#### Constraints:

- The linked list contains at least one node.

## Intuition

We can divide this problem into two objectives:

- Find the position of the kth last node.

- Remove this node.

Let’s first understand how node removal works. Consider the example below, where we need to remove node b. To do this, we need access to the node preceding it (node a), so we can redirect the pointer of node a to skip over node b. This ensures node b is no longer reachable through linked list traversal:

![Image represents a linked list data structure illustrating the removal of a node.  A rectangular box labeled 'prev' poin](./images/64d576a1_image-03-02-1-XPPCQQWL.svg)

![Image represents a state diagram illustrating a coding pattern, possibly related to state transitions or workflow.  A re](./images/1a56b606_image-03-02-2-5CMW7NAA.svg)

This indicates **we need to find the node directly before the kth last node** in order to remove it.

A naive solution to this problem is to first obtain the length of the linked list (n) by traversing it. Then, use this length to determine the number of steps required to arrive at the node before the kth last node, which is just n - k - 1 steps. This solution involves two for-loops, but is there a cleaner way to approach this problem?

The challenge with navigating a singly linked list in a single for-loop is that as we traverse, it’s hard to tell how far we are from the final node. The only way we’d know this is when we reach the final node itself, since its next node is null. How can we make use of this information?

Consider using two pointers instead of one. Could we create a scenario where, by the time one pointer reaches the end of the linked list, another pointer is positioned before the kth last node? Let’s explore this logic using the following example:

![Image represents a directed graph illustrating a sequence of nodes connected by unidirectional arrows.  The nodes are re](./images/f27a7b30_image-03-02-3-3QJ7PKK2.svg)

We denote the first pointer as leader and the pointer that follows it as trailer. When the leader pointer reaches the last node of the linked list, we want the trailer pointer to end up at node 4 (the node right before the kth last node) to prepare for deletion. In other words, the leader should be k nodes in front of the trailer when the leader reaches the last node.

![Image represents a linked list data structure illustrating a sliding window pattern with a window size (k) of 2.  The li](./images/5eeb80be_image-03-02-4-JSDDALXN.svg)

To achieve this, we can start by advancing the leader pointer through the linked list for k steps. When the leader pointer is k nodes ahead of the trailer, we can advance both pointers together until the leader reaches the last node. This process will be explained in more detail soon.

However, there’s an important edge case to consider first: **what if the head itself is the node we need to remove?** In this case, there’s no node before the head, so we cannot perform the removal, as mentioned earlier. To circumvent this, we can create a `dummy` node, place it before the head node, and start our traversal from there.

![Image represents a linked list data structure illustrating a coding pattern.  Two rectangular boxes labeled 'trailer' an](./images/324e8622_image-03-02-5-HANYJFVP.svg)

---

Let’s now try incorporating our strategy into the example.

First, advance the leader pointer k (2) times so it’s k nodes ahead of the trailer pointer:

![Image represents a linked list data structure illustrating a coding pattern.  A gray, circular node labeled 'D' represen](./images/9d468141_image-03-02-6-JIFIZVRO.svg)

---

With the leader k nodes ahead, we can move both the trailer and leader pointers until the leader reaches the last node:

![Image represents a linked list data structure illustrating the 'Leader-Follower' coding pattern.  The list is composed o](./images/1cbf246a_image-03-02-7-VXHVJNK6.svg)

![Image represents a linked list data structure illustrating the Leader-Follower pattern.  A gray circle labeled 'D' repre](./images/7b0db65d_image-03-02-8-EHB5Z7DE.svg)

![Image represents a linked list data structure illustrating the concept of pointers and multiple linked lists.  A primary](./images/1efe9b10_image-03-02-9-C5WELPUS.svg)

---

With the trailer pointer at the ideal position, we can remove node 7:

![Image represents a linked list data structure undergoing an insertion operation.  A singly linked list is depicted with ](./images/cc7a747f_image-03-02-10-TLRKZXI5.svg)

![Image represents a diagram illustrating a coding pattern, possibly related to linked lists or data structures.  The diag](./images/ef40f06a_image-03-02-11-RBLUN6LJ.svg)

After this removal, we just return `dummy.next`, which points at the head of the modified linked list.

## Implementation

```python
from ds import ListNode
    
def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # A dummy node to ensure there's a node before 'head' in case we need to remove
    # the head node.
    dummy = ListNode(-1)
    dummy.next = head
    trailer = leader = dummy
    # Advance 'leader' k steps ahead.
    for _ in range(k):
        leader = leader.next
        # If k is larger than the length of the linked list, no node needs to be
        # removed.
        if not leader:
            return head
    # Move 'leader' to the end of the linked list, keeping 'trailer' k nodes behind.
    while leader.next:
        leader = leader.next
        trailer = trailer.next
    # Remove the kth node from the end.
    trailer.next = trailer.next.next
    return dummy.next

```

```javascript
import { ListNode } from './ds.js'

export function remove_kth_last_node(head, k) {
  // A dummy node to ensure there's a node before 'head' in case we need to remove
  // the head node.
  const dummy = new ListNode(-1)
  dummy.next = head
  let trailer = dummy
  let leader = dummy
  // Advance 'leader' k steps ahead.
  for (let i = 0; i < k; i++) {
    leader = leader.next
    // If k is larger than the length of the linked list, no node needs to be
    // removed.
    if (!leader) {
      return head
    }
  }
  // Move 'leader' to the end of the linked list, keeping 'trailer' k nodes behind.
  while (leader.next) {
    leader = leader.next
    trailer = trailer.next
  }
  // Remove the kth node from the end.
  trailer.next = trailer.next.next
  return dummy.next
}

```

```java
import core.LinkedList.ListNode;

public class Main {
    public ListNode<Integer> remove_kth_last_node(ListNode<Integer> head, int k) {
        // A dummy node to ensure there's a node before 'head' in case we need to remove
        // the head node.
        ListNode<Integer> dummy = new ListNode<>(-1);
        dummy.next = head;
        ListNode<Integer> trailer = dummy;
        ListNode<Integer> leader = dummy;
        // Advance 'leader' k steps ahead.
        for (int i = 0; i < k; i++) {
            leader = leader.next;
            // If k is larger than the length of the linked list, no node needs to be
            // removed.
            if (leader == null) {
                return head;
            }
        }
        // Move 'leader' to the end of the linked list, keeping 'trailer' k nodes behind.
        while (leader.next != null) {
            leader = leader.next;
            trailer = trailer.next;
        }
        // Remove the kth node from the end.
        trailer.next = trailer.next.next;
        return dummy.next;
    }
}

```

### Complexity Analysis

**Time complexity:** The time complexity of `remove_kth_last_node` is O(n). This is because the algorithm first traverses at most n nodes of the linked list, and then two pointers traverse the linked list at most once each.

**Space complexity:** The space complexity is O(1).