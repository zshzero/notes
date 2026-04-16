# Evaluate Expression

Given a string representing a mathematical expression containing integers, parentheses, addition, and subtraction operators, evaluate and return the result of the expression.

#### Example:

```python
Input: s = '18-(7+(2-4))'
Output: 13

```

## Intuition

At first, it might seem overwhelming to deal with expressions that include a variety of elements like negative numbers, nested expressions inside parentheses, and numbers with multiple digits. The key to managing this complexity is to break down the problem into smaller, more manageable parts. Let's first focus on evaluating simple expressions that contain no parentheses.

**Handling positive and negative signs**

Consider the following expression:

![Image represents a simple arithmetic expression displayed linearly.  The expression consists of the number 28, a minus s](./images/02d34e0b_image-07-03-1-AMDAEXRA.svg)

There's already some complexity in this expression with there being two signs to consider: plus and minus. An immediate simplification we can make is to **treat all expressions as ones of pure addition**. This is possible when we assign signs to each number (1 representing + and -1 representing -). This sign can be multiplied by the number to attain its correct value. This allows us to just focus on performing additions:

![Image represents three separate instances demonstrating a concept likely related to signed numbers or data. Each instanc](./images/0fec21ad_image-07-03-2-5HZOEGR7.svg)

**Processing numbers with multiple digits**

Another complexity in this expression is that some numbers have multiple digits. We’ll need a way to build numbers digit by digit until we reach the end of the number. We can build a number using the variable `curr_num`, which is initially set to 0. Every time we encounter a new digit, we multiply `curr_num` by 10 and add the new digit to it, effectively shifting all digits to the left and appending the new digit.

We can see this process play out for the string “123” in the following illustration:

![Image represents a diagram illustrating a digit-by-digit number conversion process.  A rectangular box labeled 'digit' p](./images/8f574011_image-07-03-3-HTLV5ZR2.svg)

![Image represents a step-by-step calculation of converting a sequence of digits into a numerical value.  A rectangular bo](./images/d519a848_image-07-03-4-IHSWF7K5.svg)

![Image represents a diagram illustrating a numerical processing algorithm.  A rectangular box labeled 'digit' sits above ](./images/96c4453f_image-07-03-5-OC4X65C2.svg)

We can stop building this number once we encounter a non-digit character, indicating the end of the number.

**Evaluating an expression without parentheses**

With the information from the section above, let's evaluate the following expression, which contains no parentheses. We’ll start off with a sign of 1:

![Image represents a snapshot of a program's state during execution, likely illustrating a coding pattern related to numer](./images/22ff8f60_image-07-03-6-CAOKQBKM.svg)

---

Upon reaching the ‘-’ operator, we’ve reached the end of the first number (28). So, let’s:

- Multiply the current number (28) by its sign (1).

- Add the resulting product (28) to the result.

- Update the sign to -1 since the current operator is a minus sign.

- Reset `curr_num` to 0 before building the next number.

![Image represents a visual explanation of a coding pattern, likely related to parsing or processing numerical strings.  T](./images/6232edd5_image-07-03-7-XLYYJDZQ.svg)

---

Once we reach the second operator, we multiply the current number (10) by its sign of -1 before adding the resulting product (-10) to the result. This effectively subtracts 10 from the result:

![Image represents a step-by-step illustration of a coding pattern, likely related to number processing or parsing.  The l](./images/3d3996ba_image-07-03-8-ZUCYWO44.svg)

---

Finally, once we’ve reached the end of the string, we just add the final number (7) to the result after multiplying it by its sign of 1:

![Image represents a diagram illustrating a coding pattern, possibly related to arithmetic operations or string manipulati](./images/673ae417_image-07-03-9-TCHEWI3Y.svg)

**Evaluating expressions containing parentheses**

Now that we can solve simple expressions, it's time to bring parentheses into the discussion. Moving forward, we define a nested expression as one that’s inside a pair of parentheses.

One challenge is that we need to evaluate the results of nested expressions before we can calculate the original expression. Once all nested expressions are evaluated, we can evaluate the original expression.

![Image represents a mathematical expression structured to illustrate order of operations. The expression is '18 - (7 + (2](./images/da8c14aa_image-07-03-10-VM2352PJ.svg)

![Image represents a simple arithmetic expression depicted as a data flow diagram.  The expression is '18 - (7 - 2)'.  The](./images/74557bac_image-07-03-11-XKS7U7IH.svg)

![Image represents a simple arithmetic expression depicted as a data flow diagram.  A peach-colored, horizontally-oriented](./images/2d820ce2_image-07-03-12-IDD2YK7W.svg)

Consider another problem in this chapter that also contains parentheses: *Valid Parenthesis Expression*. In that problem, we used a **stack** to process nested parentheses in the right order. This suggests a stack might also help us evaluate nested expressions in the right order. Let’s explore this idea further.

Similar to *Valid Parenthesis Expression*, an opening parenthesis ‘`(`‘ indicates the start of a new nested expression, whereas a closing parenthesis ‘`)`’ indicates the end of one. Understanding this, let’s try to use a stack to solve the following expression.

![Image represents a visual explanation of arithmetic expression evaluation using a stack data structure.  The left side s](./images/791c2de8_image-07-03-13-DEKUIWT7.svg)

---

We already know how to evaluate expressions without parentheses, so let’s just focus on what to do when we encounter a parenthesis.

At the first opening parenthesis, we know a nested expression has started. Before we evaluate the nested expression, we’ll need to save the running result (`res`) of the current expression, as well as the sign of this upcoming nested expression. This way, once we’re done evaluating the nested expression, we can resume where we were in the current expression.

Here are the steps for when we encounter an opening parenthesis:

- `stack.push(res)`: Save the running result on the stack.

- `stack.push(sign)`: Save the sign of the upcoming nested expression on the stack.

- `res = 0`, `sign = 1`: Reset these variables because we’re about to begin calculating a new expression.

![Image represents a diagram illustrating a coding pattern, likely for evaluating arithmetic expressions using a stack.  T](./images/7d6181ba_image-07-03-14-P5GIJ3X3.svg)

![Image represents a blank, light gray square.  There are no visible components, shapes, lines, text, URLs, or any other e](./images/aab4146d_image-07-03-15-LHGJDQSB.png)

![Image represents a visual explanation of postfix notation evaluation using a stack.  The left side shows the arithmetic ](./images/0df0569b_image-07-03-16-4N6K3QJ7.svg)

---

The next parenthesis we encounter is an opening parenthesis. Again, this indicates the start of a new nested expression. Let’s save the current result and sign on the stack, before resetting them to evaluate the upcoming nested expression:

![Image represents a step-by-step illustration of evaluating an arithmetic expression using a stack.  The left side shows ](./images/0170bea5_image-07-03-17-ZCUTS23F.svg)

![Image represents a blank, light gray square.  There are no visible components, shapes, lines, text, URLs, or any other e](./images/2ee70ce5_image-07-03-18-LHGJDQSB.png)

![Image represents a visual explanation of postfix notation evaluation using a stack.  The left side shows the arithmetic ](./images/9476d3e6_image-07-03-19-R7MNE33C.svg)

---

The next parenthesis we encounter is a closing parenthesis. This means the current nested expression just ended, and we need to merge its result with the outer expression. Here’s how we do this:

- `res *= stack.pop()`: Apply the sign of the current nested expression to its result.

- `res += stack.pop()`: Add the result of the outer expression to the result of the current nested expression.

![Image represents a visual explanation of postfix expression evaluation using a stack.  The left side shows the postfix e](./images/802cd84f_image-07-03-20-IVQFHLMJ.svg)

After applying those operations, the value of `res` will be 5, representing the result of the highlighted part of the expression below:

![The image represents a visual depiction of postfix expression evaluation using a stack.  The expression '1 8 - ( 7 + ( 2](./images/6dac9527_image-07-03-21-KVIOFXMC.svg)

---

At the final closing parenthesis, we can apply the same steps:

![Image represents a visual explanation of evaluating an arithmetic expression using a stack.  The expression '1 8 - (7 + ](./images/a153561c_image-07-03-22-VUPHYOQC.svg)

Finally, the value of `res` will be 13, representing the result of the entire expression:

![Image represents a visual depiction of expression evaluation using a stack.  A mathematical expression '1 8 - ( 7 + ( 2 ](./images/be8d3d86_image-07-03-23-AYLU5ADS.svg)

Now that we’ve reached the end of the string, we can return `res`.

## Implementation

```python
def evaluate_expression(s: str) -> int:
    stack = []
    curr_num, sign, res = 0, 1, 0
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        # If the current character is an operator, add 'curr_num' to the result
        # after multiplying it by its sign.
        elif c == '+' or c == '-':
            res += curr_num * sign
            # Update the sign and reset 'curr_num'.
            sign = -1 if c == '-' else 1
            curr_num = 0
        # If the current character is an opening parenthesis, a new nested expression
        # is starting.
        elif c == '(':
            # Save the current 'res' and 'sign' values by pushing them onto
            # the stack, then reset their values to start calculating the new nested
            # expression.
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        # If the current character is a closing parenthesis, a nested expression has
        # ended.
        elif c == ')':
            # Finalize the result of the current nested expression.
            res += sign * curr_num
            # Apply the sign of the current nested expression’s result before adding
            # this result to the result of the outer expression.
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
    # Finalize the result of the overall expression.
    return res + curr_num * sign

```

```javascript
export function evaluate_expression(s) {
  const stack = []
  let currNum = 0,
    sign = 1,
    res = 0
  for (let c of s) {
    if (/\d/.test(c)) {
      currNum = currNum * 10 + parseInt(c)
    }
    // If the current character is an operator, add 'currNum' to the result
    // after multiplying it by its sign.
    else if (c === '+' || c === '-') {
      res += currNum * sign
      // Update the sign and reset 'currNum'.
      sign = c === '-' ? -1 : 1
      currNum = 0
    }
    // If the current character is an opening parenthesis, a new nested expression
    // is starting.
    else if (c === '(') {
      // Save the current 'res' and 'sign' values by pushing them onto
      // the stack, then reset their values to start calculating the new nested
      // expression.
      stack.push(res)
      stack.push(sign)
      res = 0
      sign = 1
    }
    // If the current character is a closing parenthesis, a nested expression has
    // ended.
    else if (c === ')') {
      // Finalize the result of the current nested expression.
      res += sign * currNum
      // Apply the sign of the current nested expression’s result before adding
      // this result to the result of the outer expression.
      res *= stack.pop()
      res += stack.pop()
      currNum = 0
    }
  }
  // Finalize the result of the overall expression.
  return res + currNum * sign
}

```

```java
import java.util.Stack;

public class Main {
    public Integer evaluate_expression(String s) {
        Stack<Integer> stack = new Stack<>();
        int currNum = 0, sign = 1, res = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                currNum = currNum * 10 + (c - '0');
            }
            // If the current character is an operator, add 'currNum' to the result
            // after multiplying it by its sign.
            else if (c == '+' || c == '-') {
                res += currNum * sign;
                // Update the sign and reset 'currNum'.
                sign = (c == '-') ? -1 : 1;
                currNum = 0;
            }
            // If the current character is an opening parenthesis, a new nested expression
            // is starting.
            else if (c == '(') {
                // Save the current 'res' and 'sign' values by pushing them onto
                // the stack, then reset their values to start calculating the new nested
                // expression.
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            }
            // If the current character is a closing parenthesis, a nested expression has
            // ended.
            else if (c == ')') {
                // Finalize the result of the current nested expression.
                res += sign * currNum;
                // Apply the sign of the current nested expression’s result before adding
                // this result to the result of the outer expression.
                res *= stack.pop();
                res += stack.pop();
                currNum = 0;
            }
        }
        // Finalize the result of the overall expression.
        return res + currNum * sign;
    }
}

```

### Complexity Analysis

**Time complexity:** The time complexity of `evaluate_expression` is O(n) because we traverse each character of the expression once, processing nested expressions using the stack, where each stack push or pop operation takes O(1) time.

**Space complexity:** The space complexity is O(n) because the stack can grow proportionally to the length of the expression.