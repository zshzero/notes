# Stack & Queue Interview LeetCode Exercises

### [0. Implement Stack Using a List]()

```py
class Stack:
    def __init__(self):
        self.top = -1
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)
        self.top += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        popped_element = self.stack_list.pop()
        self.top -= 1
        return popped_element
        
    def is_empty(self):
        return len(self.stack_list) == 0
        
    def print_stack(self):
        print("-----------------------------")
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
        print("-----------------------------")
```

### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

```py
# Stack and Hashmap
# Time Complexity - O(n)
# Space Complexity - O(n)
def isValid(self, s: str) -> bool:
    # create hashmap to store corresponding brackets
    brackets = {
        ')':'(', 
        '}': '{', 
        ']': '['
    }
    stack = [] 
    for ch in s:
        # pop and compare if ch is closing bracket 
        if stack and ch in brackets:
            if brackets[ch] != stack.pop():
                return False
        # else append to stack
        else:
            stack.append(ch)
    # its a valid series if stack is empty
    return False if stack else True 

# Using two-pointer approach is challenging because it typically excels in problems where you can process elements in a linear or bi-directional sweep without needing to revisit previous elements.

# Here’s why:

# Nested Structure: Parentheses can be nested arbitrarily deep. 
# Ex: For string "({[]})", you need to remember that the first parenthesis opened first, which is not possible with just two pointers.

# Order of Matching: The valid sequence is determined by the order in which opening brackets appear and their matching closing brackets. This is possible with a stack and not with two pointers. 
```

### [344. Reverse String](https://leetcode.com/problems/reverse-string)

```py
# Two Pointer
# Time Complexity - O(n)
# Space Complexity - 1
def reverseString(self, s: List[str]) -> None:
    # initialize left and right pointer
    right = len(s) - 1
    left = 0
    # swap values until middle
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

```py
# Stack
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(n)
def reverseString(self, s: List[str]) -> None:
    length = len(s)
    # initialize stack and append all chars to it
    stack = []
    for ch in s:
        stack.append(ch)

    # pop and assign them from left to right
    for i in range(length):
        s[i] = stack.pop()
```

```py
# Recursive
# Time Complexity - O(n)
# Space Complexity - O(n)
def reverseString(self, s: List[str]) -> None:
    # swap values and call itself until middle
    def reverse(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            reverse(left+1, right-1)
    # initiate call
    reverse(0, len(s)-1)
```

### [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare)

```py
# Stack
# Time Complexity - O(n + m)
# Space Complexity - O(n + m)
def backspaceCompare(self, s: str, t: str) -> bool:
    # initialize 2 stacks
    sStack = []
    tStack = []
    sLength = len(s)
    tLength = len(t)

    i = 0
    # traverse s and pop from its stack if "#" else append it
    while i < sLength:
        if sStack and s[i] == "#":
            sStack.pop()
        if s[i] != "#":
            sStack.append(s[i])
        i += 1
        
    j = 0
    # traverse t and pop from it stack if "#" else append it
    while j < tLength:
        if tStack and t[j] == "#":
            tStack.pop()
        if t[j] != "#":
            tStack.append(t[j])
        j += 1
    
    # check if both stack values are equal
    return sStack == tStack
```

```py
# Two Pointer
# Time Complexity - O(n + m)
# Space Complexity - O(1)
def backspaceCompare(self, s: str, t: str) -> bool:
    # helper method to calculate next valid index
    def findNextValidChar(word: str, index: int) -> int:
        validIndex = index
        backspaceCount = 0
        
        # loop until next valid char after considering backspace
        while validIndex >= 0:
            # returns valid index when it encounters a valid char and all backspaces are nullified 
            # reverse order of conditions to gain performance
            if word[validIndex] != '#' and backspaceCount == 0:
                # print("1")
                break
            # decr backspace count when it encounters a valid char but count isn't nullified  
            # reverse order of conditions to gain performance
            elif word[validIndex] != '#' and backspaceCount > 0:
                # print("2")
                backspaceCount -= 1
            # incr backspace count when it encounters a backspace char 
            elif word[validIndex] == '#':
                # print("3")
                backspaceCount += 1
             # move to next index as backspace count isn't nullified yet
            validIndex -= 1
        return validIndex

    sPtr = len(s) - 1
    tPtr = len(t) - 1
    # traverse from right to left of the strings
    while sPtr >= 0 or tPtr >= 0:
        # find next valid index
        sPtr = findNextValidChar(s, sPtr) 
        tPtr = findNextValidChar(t, tPtr)
        # print(sPtr,tPtr)

        # get corresponding char (set "" when index goes out of bound)
        sch = s[sPtr] if sPtr >= 0 and s[sPtr] else ""
        tch = t[tPtr] if tPtr >= 0 and t[tPtr] else ""

        # return false when char doesn't match
        if sch != tch:
            return False

        sPtr -= 1
        tPtr -= 1

    return True
```

### [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks)

```py
class MyQueue:
    def __init__(self, value = None):
        if not value:
            self.stack1 = []
        else:        
            self.stack1.append(value)
        self.stack2 = []
        
    def peek(self):
        peekIndex = len(self.stack1) - 1
        return self.stack1[peekIndex]
    
    def is_empty(self):
        return len(self.stack1) == 0
        
    def enqueue(self, value):
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(value)
        
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
            
        return True
            
    def dequeue(self):
        if not self.stack1:
            return
        
        return self.stack1.pop()
```

```py
class MyQueue:
    def __init__(self):
        # create 2 stacks, for enqueue and dequeue each 
        self.enStack = []
        self.deStack = []

    def push(self, x: int) -> None:
        return self.enStack.append(x)

    def pop(self) -> int:
        self.isDeStackEmpty()
        return self.deStack.pop()

    def peek(self) -> int:
        self.isDeStackEmpty()
        return self.deStack[-1]

    def empty(self) -> bool:
        return len(self.enStack) == 0 and len(self.deStack) == 0

    # push elements from enqueue stack to dequeue once its empty
    def isDeStackEmpty(self):
        if self.deStack:
            return
        
        for _ in range(len(self.enStack)):
            self.deStack.append(self.enStack.pop())
```