### Intro

- Function which calls itself (recursive case) until break condition (base case) is satisfied and returned
  - Way of calling recursive function is the same always
  - For every recursive function call, the problem gets smaller

### Call Stack

-  Call Stack keeps track of function calls in the order they occur
  - It stores information about active functions which helps in managing control flow of the program
- Each recursive call adds a new stack frame to call stack
  - If recursion is too deep, then it can lead to stack overflow, where call stack runs out of memory
- Using debugger in VS Code

### Factorial

```py
def factorial(n: int) -> int:
  if n == 1: # Base case: 1!
    return 1
  # repeating same thing over and over
  return n * factorial(n - 1) # problem is getting smaller 
```