# Swap Odd and Even Bits

Given an unsigned 32-bit integer `n`, return an integer where all of `n`'s even bits are **swapped** with their adjacent odd bits.

#### Example 1:

![Image represents a diagram illustrating a binary addition process.  The diagram shows two rows of binary numbers, repres](./images/ec1d6008_swap-odd-and-even-bits1-765WVD32.svg)

```python
Input: n = 41
Output: 22

```

#### Example 2:

![Image represents a diagram illustrating a data transformation or processing step, possibly within a coding pattern relat](./images/9e950f63_swap-odd-and-even-bits2-KNYQUWJJ.svg)

```python
Input: n = 23
Output: 43

```

## Intuition

Swapping even and odd bits means that each bit in an even position is swapped with the bit in the next odd position, and vice versa. Note that the positions start at position 0, which is the position of the least significant bit.

The key thing to notice is that, in order to perform the swap:

- All bits in the even positions need to be shifted one position to the left.

- All bits in the odd positions need to be shifted one position to the right.

![Image represents a visual depiction of a bitwise XOR operation across multiple positions.  The top row displays 'positio](./images/c2a81340_image-18-03-1-QKLL25QR.svg)

This suggests that if we had a way to extract all the even and odd-positioned bits separately, we could shift them accordingly and then merge them back together, so the odd-positioned bits are in the even positions, and vice versa.

![Image represents a flowchart illustrating a bit manipulation algorithm.  At the top, a sequence of bits '1 0 1 0 0 1' is](./images/094e0cf1_image-18-03-2-GR7VPIZR.svg)

Let’s start by figuring out how to obtain the even and odd bits of n.

**Obtaining all even bits**

To obtain all even bits of n, we can use a mask which has all even bit positions set to 1:

![Image represents a visual depiction of an 'even mask' applied to a sequence of numbers.  The top row displays a sequence](./images/58e5187f_image-18-03-3-4SOTVC3V.svg)

Performing a bitwise-AND with this mask and n gives us an integer where all the bits at odd positions are set to 0, ensuring only the bits in even positions of n are preserved:

![Image represents a bitwise AND operation demonstrating how to extract even-indexed bits from a binary sequence.  The top](./images/d22e0d1a_image-18-03-4-45CDA5ZJ.svg)

**Obtaining all odd bits**

Similarly, to obtain all the odd bits of n, we can use a mask with all odd bit positions are set to 1:

![Image represents a visual depiction of an odd mask applied to a sequence of numbers.  The top row displays a sequence of](./images/e17f966c_image-18-03-5-Q6XAAVIX.svg)

Performing a bitwise-AND with this mask and n gives us an integer where all the bits at even positions are set to 0, ensuring only the bits at odd positions of n are preserved:

![Image represents a bitwise AND operation to extract odd bits from a binary sequence.  The top row shows a binary sequenc](./images/7bc1f06d_image-18-03-6-GUNXXBSV.svg)

Now that we’ve extracted all the even bits and odd bits separately, let’s use them to obtain the result, where the bits at odd and even positions are swapped.

**Shifting and merging the bits at odd and even positions**

We can use the shift operator to shift the bits at even positions to the left once, and the bits at odd positions to the right once:

![Image represents two parallel rows of data transformations.  The top row shows a sequence of numbers, primarily zeros, w](./images/c12cb135_image-18-03-7-JWAI3ESP.svg)

Then, to merge these together, we can use the bitwise-OR operator because it combines the two sets of bits into the final result.

![Image represents a bitwise OR operation illustrated using two rows of bits and a result row.  The top row, labeled '(shi](./images/eedf2738_image-18-03-8-25JBL66S.svg)

Now, the odd-positioned bits are in the even positions and vice versa.

## Implementation

```python
def swap_odd_and_even_bits(n: int) -> int:
    even_mask = 0x55555555   # 01010101010101010101010101010101
    odd_mask = 0xAAAAAAAA  # 10101010101010101010101010101010
    even_bits = n & even_mask
    odd_bits = n & odd_mask
    # Shift the even bits to the left, the odd bits to the right, and merge these
    # shifted values together.
    return (even_bits << 1) | (odd_bits >> 1)

```

```javascript
export function swap_odd_and_even_bits(n) {
  const evenMask = 0x55555555 // 01010101010101010101010101010101
  const oddMask = 0xaaaaaaaa // 10101010101010101010101010101010
  const evenBits = n & evenMask
  const oddBits = n & oddMask
  // Shift the even bits to the left, the odd bits to the right, and merge these
  // shifted values together.
  return (evenBits << 1) | (oddBits >>> 1)
}

```

```java
public class Main {
    public Integer swap_odd_and_even_bits(int n) {
        int evenMask = 0x55555555;  // 01010101010101010101010101010101
        int oddMask = 0xAAAAAAAA;   // 10101010101010101010101010101010
        int evenBits = n & evenMask;
        int oddBits = n & oddMask;
        // Shift the even bits to the left, the odd bits to the right, and merge these
        // shifted values together.
        return (evenBits << 1) | (oddBits >>> 1);
    }
}

```

### Complexity Analysis

**Time complexity**: The time complexity of `swap_odd_and_even_bits` is O(1).

**Space complexity:** The space complexity is O(1).