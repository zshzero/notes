# Introduction to Linked Lists

## Intuition

A linked list is a data structure consisting of a sequence of nodes, where each node is linked to the next. A node in a linked list has two main components: the data it stores (`val`) and a reference to the next node (`next`) in the sequence:

![The image represents a single node in a linked list data structure.  A circular node, outlined in black, contains the la](./images/443c4ad2_image-03-00-1-6ZCQNYMW.svg)

We define a node using the `ListNode` class, as below:

```python
class ListNode:
   def __init__(self, val: int, next: ListNode):
       self.val = val
       self.next = next

```

```javascript
class ListNode {
  constructor(val = null, next = null) {
    this.val = val
    this.next = next
  }
}

```

```java
class ListNode<T> {
    T val;
    ListNode next;
    ListNode(T val) {
        this.val = val;
        this.next = null;
    }
}

```

**Singly linked list**

The simplest form of a linked list is a singly linked list, where each node points to the next node in the linked list, and the last node points to nothing (null), indicating the end of the linked list. The start of the linked list is called the ‘head,’ which is generally the only node we initially have immediate access to:

![Image represents a singly linked list data structure.  A rectangular box labeled 'head' points downwards to a circle con](./images/2221f7ed_image-03-00-2-AT2F3OFH.svg)

To access the other nodes in a linked list, we would need to traverse it starting at the head.

![Image represents a singly linked list data structure.  Five circular nodes, numbered 1 through 5, are depicted, each con](./images/669e3836_image-03-00-3-AEN6R2C4.svg)

Singly linked lists can be used to store a collection of data. One of their main benefits lies in their **dynamic sizing** capability, since they can grow or shrink in size flexibly, unlike arrays which are fixed in size. Additionally, singly linked lists excel in scenarios requiring **frequent insertions and deletions**, as these operations can be performed more efficiently than in arrays, which need to shift elements to perform insertion or deletion.

![Image represents a visual explanation of inserting a node into a linked list.  The top section shows an initial linked l](./images/0d9b8d62_image-03-00-4-CPLT3N7N.svg)

The efficiency of these operations comes at the cost of the **inability to perform random access,** as nodes can’t be accessed by indexes like in an array. This trade-off may be acceptable in many use cases where the benefits of dynamic sizing and the efficiency of insertion/deletion outweigh the main performance benefits of random access.

**Doubly linked list**

A doubly linked list is an extended version of the linked list where each node contains two references: one to the next node (`next`), and one to the previous node (`prev`). In most implementations, doubly linked lists have immediate access to both the head node and the tail node.

![Image represents a doubly linked list data structure.  Five nodes, numbered 1 through 5, are depicted as circles, each c](./images/b8ecd089_image-03-00-5-OWLQV5EV.svg)

A big advantage of doubly linked list is that it allows for **bidirectional traversal**. Additionally, deleting nodes in a doubly linked list is generally more straightforward because we have references to both the next and previous nodes:

![Image represents a doubly linked list before and after the deletion of a node.  The top half shows the initial state: a ](./images/2b61653d_image-03-00-6-UH3I5OIY.svg)

## Pointer Manipulation

Many linked list interview problems require traversing or restructuring a linked list. Understanding and being proficient at pointer manipulation is essential to solving these problems. A useful tip is to visualize pointers as arrows that point from one node to another, and observe how these arrows should be moved to reflect the structural change. For example, this is how we would visualize a node insertion:

![Image represents a visual depiction of inserting a new node into a linked list.  The top shows a labeled orange rectangl](./images/23278fb6_image-03-00-7-ITUSUVPQ.svg)

## Real-world Example

**Music Playlist**: Music player applications often use linked lists to implement playlists, particularly doubly linked lists, where each song node links to the next and previous songs. This structure enables efficient addition, removal, and reordering of songs because only the pointers between nodes need to be updated, rather than moving the song data in memory.

## Chapter Outline

In this chapter, we explore problems involving both singly and doubly linked lists. We also explore the unique challenge of restructuring a multi-level linked list.

![Image represents a hierarchical diagram illustrating different coding patterns related to linked lists.  A rounded recta](./images/9d5a349a_image-03-00-8-GPF2JS53.svg)