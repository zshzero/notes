### Intro

- Array vs List - [Link](https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/)

  - vector containing homogeneous elements allocated with contiguous memory locations - size of array is fixed.
  - collection of elements of multiple data types supporting negative indexing
  - insertion and Deletion costs high in array as compared to List however indexing is fast in the Arrays due to contiguous memory allocation

- Linked List - [Link](https://www.geeksforgeeks.org/what-is-linked-list/)
  - structure that is made of a chain of nodes. Every node contains a value and a pointer to the next node - the elements are linked using pointers - easy to insert and erase

### Big O - Comparing chart with list in dir

- Lookup by Value or Index
  - Lookup needs iterating the list - finding by index or value needs traversing from head till match
- Append a new node at the end - O(1)
  - adding a node at the end is always constant
- Pop a node at the end - O(n)
  - removing a node at the end needs iterating the list - to find pointer that points to the node before the last node
- Append a new node at the beginning - O(1)
  - adding a node at the beginning is always constant
- Pop a new node at the beginning - O(1)
  - removing a node at the beginning is always constant
- Append a new node in between - O(n)
  - adding a node in between needs iterating the list - find the node by index or value
- Pop a new node in between - O(n)
  - removing a node in between needs iterating the list - find the node by index or value

### Under the hood

- A node will contain its value and a pointer that points to next node
- Illustration of a linked list
  ![LinkedList](https://i.imgur.com/RhP2Ppd.png)
- Actual structure of linked list
  ![LinkedList](https://i.imgur.com/NgMAtD7.png)

### Constructor

```py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

linkedList = LinkedList(4)

print(linkedList.head.value)
```

### Print LL

```py
def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
```

### Append LL

![Create a Node](https://i.imgur.com/xAILgb9.png)
![Point the next of tail to new Node](https://i.imgur.com/VB4UvHR.png)
![Point tail to new Node](https://i.imgur.com/8Ctm9Cu.png)

- Edge Case: When there are no elements in LL
  ![No elements in LL](https://i.imgur.com/YyS2BX2.png)
  ![Point head and tail to new node](https://i.imgur.com/C9f4GXA.png)

```py
def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
```

### Pop LL

![Existing LL](https://i.imgur.com/nBIlgqF.png)
![Detach the tail node and return it](https://i.imgur.com/QaE9GwY.png)

- Visualizing structural level
  ![Existing LL](https://i.imgur.com/geVTfmf.png)
  ![Point tail to previous node](https://i.imgur.com/1AzZ5gX.png)
  ![Detach the last node](https://i.imgur.com/zctPNV7.png)
  ![Return the last node](https://i.imgur.com/BpznZ1I.png)

- Coding Logic
  ![Assign two temp vars pointing head](https://i.imgur.com/dOCn1kj.png)
  ![Traverse through the list](https://i.imgur.com/yF6mlwt.png)
  ![Traverse till node where next is none](https://i.imgur.com/QVO1urN.png)
  ![Point pre to tail](https://i.imgur.com/ipuEde0.png)
  ![Detach the node that tail is pointing to](https://i.imgur.com/rvOfW12.png)
  ![Return temp which was pointing to last node](https://i.imgur.com/pSFzLsJ.png)

- Edge Case: When there are no elements in LL
  ![No elements in LL](https://i.imgur.com/p24NENB.png)
  ![Return None](https://i.imgur.com/PvsggVT.png)

- Edge Case: When there are only one elements in LL
  - Reason:
    ![Loop will failing as the element if pointing to None ](https://i.imgur.com/TM6vRqY.png)
    ![Tail is already pointing to pre](https://i.imgur.com/AKGoZOU.png)
    ![Next of tail is already none](https://i.imgur.com/OfyGRo5.png)
    ![Decrement the length by 1](https://i.imgur.com/5uSw9p5.png)
  - Fix:
    ![Check for Length again](https://i.imgur.com/oujzqoO.png)
    ![Point head and tail to none](https://i.imgur.com/dRIJp8v.png)

```py
def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
```

### Prepend LL

![Create a Node](https://i.imgur.com/ZKygyEE.png)
![Point to head](https://i.imgur.com/rXSWJIh.png)
![Point head to new node](https://i.imgur.com/Gxpga7D.png)

- Edge Case: When there are no elements in LL
  ![No elements in LL](https://i.imgur.com/lcakuFh.png)
  ![Point head and tail to new node](https://i.imgur.com/C9f4GXA.png)

```py
def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
```

### Pop_First LL

![Existing LL](https://i.imgur.com/v6VAq4b.png)
![Point a temp variable to the first node](https://i.imgur.com/e8chMUp.png)
![Point head to the second node](https://i.imgur.com/gARVjm4.png)
![Point temp var to None](https://i.imgur.com/ZKb6XCI.png)

- Edge Case: When there are no elements in LL
  ![No elements in LL](https://i.imgur.com/p24NENB.png)
  ![Return None](https://i.imgur.com/PvsggVT.png)

- Edge Case: When there are only one elements in LL
  - Reason:
    ![Assigning temp to only node](https://i.imgur.com/FHgth8e.png)
    ![Point next of head to current node which is none](https://i.imgur.com/PLKYKcl.png)
    ![Point next of temp to none which is already none](https://i.imgur.com/t5gzTwu.png)
    ![Decrement the length by 1](https://i.imgur.com/P0qzFeA.png)
  - Fix:
    ![Check for Length again](https://i.imgur.com/lV8G3sU.png)
    ![Point tail to none](https://i.imgur.com/mpBSIag.png)

```py
def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
```

### Get

![Existing LL](https://i.imgur.com/pc1bw6P.png)
![Assign a temp var](https://i.imgur.com/e9wgHjp.png)
![Iterate to that index](https://i.imgur.com/mpPTGQM.png)

- Edge Case: Check if its a valid index
  ![Negative index](https://i.imgur.com/aDlgmXt.png)
  ![Out of bound index](https://i.imgur.com/Si4OjLC.png)
  - Fix: Check if index is between 0 and length

```py
def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
```

### Set

![Existing LL](https://i.imgur.com/elSdAwk.png)
![Get node by Get method and set it to temp](https://i.imgur.com/vrtBLUk.png)
![Change value of pointer](https://i.imgur.com/zNN4t9L.png)

```py
def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
```

### Insert

![Existing LL](https://i.imgur.com/hOP5AUA.png)
![Create Node for particular index](https://i.imgur.com/QHnYlEB.png)
![Create a temp var before the index](https://i.imgur.com/336uCBH.png)
![Point new node to next of temp](https://i.imgur.com/fNicAlv.png)
![Point the temp to new node](https://i.imgur.com/jJAPlLs.png)

- Edge Case: if index is less than 0
  ![Check if index is less than 0](https://i.imgur.com/Cb3mKFy.png)
- Edge Case: if index is greater than length of LL
  ![Check if index is greater than length of LL](https://i.imgur.com/addX3PN.png)
- Edge Case: index is 0
  ![Prepend if index is 0](https://i.imgur.com/xcgGkHe.png)
- Edge Case: index is length of LL
  ![Append if index is length of LL](https://i.imgur.com/o8h9n0w.png)

```py
def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
```

### Remove

![Existing LL](https://i.imgur.com/hOP5AUA.png)
![Create temp and prev var](https://i.imgur.com/dKoqXaJ.png)
![Point prev to next of temp](https://i.imgur.com/varuwID.png)
![Set next of temp to None](https://i.imgur.com/m2Lstbx.png)

- Edge Case: if index is valid
  ![Check if index is valid](https://i.imgur.com/A9wu2nh.png)
- Edge Case: index is 0
  ![Pop_First if index is 0](https://i.imgur.com/KUkC17h.png)
- Edge Case: index is length of LL
  ![Pop if index is length of LL](https://i.imgur.com/KFVwMDk.png)

```py
def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
```

### Reverse

![Existing LL](https://i.imgur.com/SpH4B5D.png)
![Create temp var and point to head](https://i.imgur.com/eGfzjty.png)
![Point head to tail](https://i.imgur.com/v10QTku.png)
![Point tail to temp](https://i.imgur.com/fbz2o9q.png)
![Create before and after var](https://i.imgur.com/qJ5vMxm.png)
![Iterate the LL](https://i.imgur.com/O4pagYt.png)
![Point after to next of temp](https://i.imgur.com/eCKdozD.png)
![Point next of temp to before](https://i.imgur.com/85Topw4.png)
![Point next of temp to before](https://i.imgur.com/MtK4prC.png)
![Point next of temp to before](https://i.imgur.com/Jq4rmFn.png)

- Iteration Logic
  ![](https://i.imgur.com/zIFRSWh.png)
  ![](https://i.imgur.com/NsDLPl8.png)
  ![](https://i.imgur.com/SfXD9RM.png)
  ![](https://i.imgur.com/hWZI5TA.png)
  ![](https://i.imgur.com/pAAXjeo.png)
  ![](https://i.imgur.com/j5TZbjV.png)
  ![](https://i.imgur.com/FBQ87ET.png)
  ![](https://i.imgur.com/8dgyQsg.png)
  ![](https://i.imgur.com/tWHS3wb.png)
  ![](https://i.imgur.com/knEBxGH.png)
  ![](https://i.imgur.com/KNcCnOc.png)
  ![](https://i.imgur.com/Ru312Uh.png)

```py
def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
```
