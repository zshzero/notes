# Linked List Reversal

Reverse a singly linked list.

#### Example:

![Image represents two directed acyclic graphs (DAGs) arranged vertically.  The top DAG consists of five nodes labeled 1, ](./images/ad76d05d_linked-list-reversal-TFWR7ODD.svg)

## Intuition - Iterative

A naive strategy is to store the values of the linked list in an array and reconstruct the linked list by traversing the array in reverse order. However, this solution does not reverse the original linked list; it just creates a new one. Could we try performing the reversal in place?

Let’s think about the problem in terms of pointer manipulation. The key observation here is that if we "flip" the direction of the pointers, we're effectively reversing the linked list:

![Image represents a visual illustration of a sequence reversal. The top row, labeled 'original:', shows a directed acycli](./images/830101aa_image-03-01-1-3IRSAE57.svg)

Now, we just need to figure out how to perform this pointer manipulation. Consider the example below:

![Image represents a simple directed acyclic graph (DAG) illustrating a sequential process or workflow.  The graph consist](./images/c78894e7_image-03-01-2-CHIYGAUJ.svg)

---

To reverse the direction of all pointers, we iterate through the nodes one by one. In this process, we need access to the current node (`curr_node`) and the previous node (`prev_node`) to adjust the current node's next pointer to the previous node. Note that `prev_node` will initially point at null since the first node has no previous node:

![Image represents a diagram illustrating a coding pattern, possibly related to linked lists or similar data structures.  ](./images/9b266f72_image-03-01-3-YNZPMF7E.svg)

![Image represents a linked list data structure illustrating a node deletion operation.  Two rectangular boxes labeled 'pr](./images/f85a7c75_image-03-01-4-VFPRPSI4.svg)

---

To reverse the next pointer, we'll need a way to shift the `curr_node` and `prev_node` pointers one node over. To shift `prev_node`, we can set it to the position of `curr_node`. However, we can't move `curr_node` to node 2 because we lost our reference to node 2:

![Image represents a linked list data structure undergoing a deletion operation.  At the top, two orange rectangular boxes](./images/1f113816_image-03-01-5-OLJE5L2N.svg)

This suggests we should have preserved a reference to node 2 **before** reversing the `curr_node`. This can be done by creating a variable `next_node` and setting it to `curr_node.next`. Let’s assume we did this. Now, we can advance `prev_node` and `curr_node` forward by one:

![Image represents a linked list data structure illustration.  Three orange rectangular boxes labeled 'prev_node', 'curr_n](./images/f377a635_image-03-01-6-TDSMQ64U.svg)

![Image represents a linked list data structure illustrating a traversal process.  Three circular nodes, labeled '1', '2',](./images/3ff612e8_image-03-01-7-OT4LOR7J.svg)

Note, we don't need to shift `next_node`, as it can be set by `curr_node.next` in the next iteration.

We can summarize this logic in three steps. At each node in the linked list:

- Save a reference to the next node (`next_node = curr_node.next`).

- Change the current node’s next pointer to link to the previous node (`curr_node.next = prev_node`).

- Move both `prev_node` and `curr_node` forward by one (`prev_node = curr_node`,`curr_node = next_node`).

---

Let's repeat these steps for the rest of the linked list:

![Image represents a diagram illustrating a linked list reversal algorithm.  The left side shows a linked list with three ](./images/f66549bf_image-03-01-8-YOKZCWJ6.svg)

![Image represents a singly linked list data structure, illustrating the concept of traversing it in reverse. Three circul](./images/1b413d6c_image-03-01-9-6F6WTJQL.svg)

---

![Image represents a linked list data structure illustrating a traversal algorithm.  Three circular nodes labeled '1', '2'](./images/55865666_image-03-01-10-7FXBAPRO.svg)

![Image represents a singly linked list data structure with three nodes labeled 1, 2, and 3.  The nodes are connected by s](./images/5eba2d01_image-03-01-11-ZP5QH7IH.svg)

---

![Image represents a diagram illustrating a linked list reversal algorithm.  Three circular nodes labeled '1,' '2,' and '3](./images/dce1b00d_image-03-01-12-YQLGHPUX.svg)

![The image represents a singly linked list data structure with three nodes, labeled 1, 2, and 3, visually depicted as cir](./images/9fb863c8_image-03-01-13-UJXY4PRR.svg)

---

![Image represents a singly linked list with three nodes labeled 1, 2, and 3, respectively.  The list is depicted visually](./images/fe195ec5_image-03-01-14-QFH57XDN.svg)

![Image represents a singly linked list with three nodes containing the values 1, 2, and 3, respectively.  The list is dep](./images/d9ad3b19_image-03-01-15-RSGSOQIE.svg)

We can stop the reversal when `curr_node` becomes null, indicating there are no more nodes to reverse.

The final step is to return the head of the reversed linked list, which is pointed to by `prev_node` once `curr_node` becomes null.

## Implementation - Iterative

```python
from ds import ListNode
   
def linked_list_reversal(head: ListNode) -> ListNode:
    curr_node, prev_node = head, None
    # Reverse the direction of each node's pointer until 'curr_node' is null.
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
curr_node = next_node # 'prev_node' will be pointing at the head of the reversed linked list.
return prev_node

```

```javascript
import { ListNode } from './ds.js'

export function linked_list_reversal(head) {
  let currNode = head
  let prevNode = null
  // Reverse the direction of each node's pointer until 'currNode' is null.
  while (currNode) {
    const nextNode = currNode.next
    currNode.next = prevNode
    prevNode = currNode
    currNode = nextNode
  }
  // 'prevNode' will be pointing at the head of the reversed linked list.
  return prevNode
}

```

```java
import core.LinkedList.ListNode;

public class Main {
    public static ListNode<Integer> linked_list_reversal(ListNode<Integer> head) {
        ListNode<Integer> currNode = head;
        ListNode<Integer> prevNode = null;
        // Reverse the direction of each node's pointer until 'currNode' is null.
        while (currNode != null) {
            ListNode<Integer> nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }
        // 'prevNode' will be pointing at the head of the reversed linked list.
        return prevNode;
    }
}

```

### Complexity Analysis

**Time complexity:** The time complexity of `linked_list_reversal` is O(n), where n denotes the length of the linked list. This is because we perform constant-time pointer manipulation at each node of the linked list.

**Space complexity:** The space complexity is O(1).

## Intuition - Recursive

Sometimes, the interviewer may want the problem solved using recursion. Let’s see what a recursive solution to this problem would look like.

In a recursive solution, the problem is solved by **solving smaller instances of the same problem**. To solve these smaller subproblems, we would need to use the linked list reversal function (`linked_list_reversal`) in its own implementation. The process of solving smaller problems using recursive calls continues until the smallest version of the problem is solved.

The smallest version of this problem involves reversing a linked list of size 0 or 1. These are linked lists which are inherently the same as their reverse. So, these can be our **base cases**.

With this in mind, let's try crafting the logic of the recursive function using the example below:

![Image represents a linked list data structure.  A rectangular box labeled 'head' points downwards to a circle containing](./images/50711eb4_image-03-01-16-PEACUQHN.svg)

---

Think about which subproblem we should solve. To reverse the entire linked list, we can use our `linked_list_reversal` function to **reverse the sublist after the current node**. This way, we only need to focus on reversing the pointer of the current node. Let’s see how this works.

As mentioned, let’s first recursively call `linked_list_reversal` on the sublist starting at `head.next`. Let’s assume this recursive call reverses this sublist and returns its head as intended.

> 
> 
> When designing a recursive function, assume any recursive call to that function will behave as intended, even if the function hasn’t been fully implemented.
> 
> 

![Image represents a singly linked list data structure undergoing reversal.  A rectangular box encloses nodes numbered 2, ](./images/423152e6_image-03-01-17-SD7RNZUB.svg)

![Image represents a linked list data structure before and after an insertion operation.  A gray rectangular box labeled '](./images/1d7f4985_image-03-01-18-TLRMYEZ6.svg)

---

Next, we need the tail of the reversed sublist (node 2) to point to node 1. We can reference node 2 using `head.next`. So, all we need to do is set `head.next.next` to head as illustrated below:

![Image represents a linked list data structure before and after inserting a new node.  Initially, a linked list is shown ](./images/60a396ad_image-03-01-19-DM7SPWQ7.svg)

![Image represents a linked list data structure illustrating an insertion operation.  Two rectangular boxes labeled 'head'](./images/8a705289_image-03-01-20-SUCMHIXI.svg)

---

The linked list is almost fully reversed now, but node 1 is still pointing to node 2. To remove this link, just set `head.next` to null. Then, we can return `new_head`, which is the head of the reversed linked list:

![Image represents a linked list data structure before and after inserting a new node at the head.  Initially, a linked li](./images/1996e00e_image-03-01-21-Z4J3KDIT.svg)

![Image represents a linked list data structure before and after insertion of a new node.  On the left, a linked list is s](./images/b0d1d3af_image-03-01-22-QAWB5JCC.svg)

## Implementation - Recursive

```python
from ds import ListNode
   
def linked_list_reversal_recursive(head: ListNode) -> ListNode:
    # Base cases.
    if (not head) or (not head.next):
        return head
    # Recursively reverse the sublist starting at the next node.
    new_head = linked_list_reversal_recursive(head.next)
    # Connect the reversed sublist to the head node to fully reverse the entire linked list.
    head.next.next = head
    head.next = None
    return new_head

```

```javascript
import { ListNode } from './ds.js'

export function linked_list_reversal_recursive(head) {
  // Base cases.
  if (!head || !head.next) {
    return head;
  }
  // Recursively reverse the sublist starting at the next node.
  const newHead = linked_list_reversal_recursive(head.next);
  // Connect the reversed sublist to the head node to fully reverse the entire linked list.
  head.next.next = head;
  head.next = null;
  return newHead;
}

```

### Complexity Analysis

**Time complexity:** The time complexity of `linked_list_reversal_recursive` is O(n) because it involves a single recursive traversal through the linked list, visiting each node exactly once.

**Space complexity:** The space complexity is O(n) due to the stack space taken up by the recursive call stack, which grows up to n levels deep because n recursive calls are made.

## Interview Tip

*Tip: Visualize pointer manipulations.*

Often, it can be tricky to figure out exactly what to do when dealing with linked list manipulation. Drawing pointers as arrows between nodes can be quite helpful. By observing how these arrows should be reoriented to represent changes in the linked list's structure, we can deduce the necessary pointer manipulation logic. This approach also helps identify which nodes we need references to when making these changes.