### Intro

- Time And Space Complexity
  - Used to compare different codes mathmatically about how efficient they run

### Worst Case

- Omega(Best Case), Theta(Average Case) and Omicron(Worst Case)
- Link to all images - [Medium](https://medium.com/@tretuna/elucidating-the-complexity-of-the-big-o-part-1-4b17aa0536c8)  
  ![Graph](https://miro.medium.com/v2/resize:fit:640/format:webp/1*MojRMNBNOHLqwe5ak7hTug.png)

##### Side Note - `O(n log n), O(2^n) and O(n!) are rarely used complexities`

### O(n)

- Ex: Print Items using for loop  
  ![Graph](https://miro.medium.com/v2/resize:fit:640/format:webp/1*axwuCvPCUm3VXOeqyOZCeQ.png)

### Drop Constants

- Numerics are not considered in complexity. Ex: O(2n) is considered as O(n)

### O(n^2)

- Ex: Print 2D matrix using for loop

##### Note - When printing 3D matrix, its not n^3, its simplified as n^2

![Graph](https://miro.medium.com/v2/resize:fit:640/format:webp/1*VTTA7FDijlC_xHbahg7OIA.png)

### Drop Non-Dominants

- Non dominants variable in the equation are not considered in complexity. Ex: O(n^2+n) is considered as O(n^2)

### O(1)

- Ex: Adding 2 numbers  
  ![Graph](https://miro.medium.com/v2/resize:fit:640/format:webp/1*iZPhN5fdAW8mFnap3FOj1w.png)

### O(log n)

- Ex: Binary search algorithm.
  - Here, for list of 8 elements, we need 3 steps
  - So, equation would be 2^3 = 8
  - Apply log, it would be log 8 base 2 = 3  
    ![Graph](https://miro.medium.com/v2/resize:fit:640/format:webp/1*y9-T7eJEIF5UaFt97LIFAQ.png)

### Different Terms of Input

- If a method has multiple params as inputs, then cant be clubbed together
  - Ex: If a method takes 2 params a, b and has its own for loop then its O(a + b) not O(n + n) = O(n)
  - Ex: If a method takes 2 params a, b and has a nested for loop then its O(a \* b) not O(n \* n) = O(n^2)

### Lists

- Append and pop is O(1) as its dealing with the last element in list and other elements are not disturbed
- Insert and pop based on index is O(n) as the elements are rearranged when element is added or removed at certain index
- Find by value is O(n) as it has to traverse the list and find by index is O(1) as it directly goes to the index

### Wrap Up

```
O(n^2) - Loop Within a Loop
O(n) - Proportional
O(log n) - Divide and Conquer
O(1) - Constant
```

Reference site - [Big-O Complexity chart](https://www.bigocheatsheet.com/)

- All of the DS discussed here is O(n)
- Choice of sorting Algos should depend on which complexity is favoured for efficiency
