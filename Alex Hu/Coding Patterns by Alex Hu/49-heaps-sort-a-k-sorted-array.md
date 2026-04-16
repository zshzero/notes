# Sort a K-Sorted Array

Given an integer array where each element is at most `k` positions away from its sorted position, **sort the array** in a non-decreasing order.

#### Example:

```python
Input: nums = [5, 1, 9, 4, 7, 10], k = 2
Output: [1, 4, 5, 7, 9, 10]

```

## Intuition

In a k-sorted array, each element is at most k indexes away from where it would be in a fully sorted array. We can visualize this with the following example where k = 2, and no number is more than k indexes away from its sorted position:

![Image represents a visual depiction of sorting a k-sorted array where k=2.  The top row shows the unsorted input array `](./images/e3dfad58_image-08-04-1-LMP2WLBK.svg)

A trivial solution to this problem is to sort the array using a standard sorting algorithm. However, since the input is partially sorted (k-sorted), we should assume there's a faster way to sort the array.

We can think about this problem backward. For any index `i`, **the element that belongs at index `i` in the sorted array is located within the range [`i` - `k`, `i` + `k`]**. Below, we visualize how number 7, which is meant to be at index 3 when sorted, correctly falls within the range [3 - `k`, 3 + `k`] in the k-sorted array:

![Image represents a visual explanation of a sorting algorithm, likely illustrating a concept related to k-sorted arrays. ](./images/ff6881ec_image-08-04-2-KL6SW5XD.svg)

This is a good start, but we can reduce this range even further. Consider index 0 from the above array. We know the number which belongs at index 0 when sorted is somewhere in the range [0, 0 + `k`]:

![Image represents a visual explanation of sorting a k-sorted array.  The top row shows a 'k-sorted array' [5, 1, 9, 4, 7,](./images/be5dcbc0_image-08-04-3-2NYAFKPN.svg)

Note that the sorted array in the diagrams is purely provided as a reference point. We don't yet know which number in the range [0, 0 + `k`] belongs at index 0. However, one fact remains consistent: in a sorted array, index 0 always holds the smallest number. This means the value needed at index 0 is also the smallest number within the range [0, 0 + `k`] of the k-sorted array, which is 1 in this example.

So, let's swap 1 with the number at index 0 to position 1 as the first value in the sorted array:

![Image represents a step-by-step illustration of a sorting algorithm applied to a k-sorted array.  The top line shows an ](./images/aa9cb47f_image-08-04-4-X37R6NX6.svg)

---

Now let's find the number that belongs at index 1: the second smallest number. Since index 0 currently contains the smallest value in the array, we won't need to consider index 0 in our search. Therefore, we can find the value that belongs at index 1 in the range [1, 1 + k]. The smallest value in this range will be the second smallest value overall, which is 4 in this case.

So, let's swap 4 with the number at index 1 to position 4 as the second value in the sorted array:

![Image represents a step-by-step illustration of a sorting algorithm applied to a k-sorted array.  The top section shows ](./images/b008ec9e_image-08-04-5-ODZXDX2H.svg)

---

If we continue this process for the rest of the array, we'll successfully sort the k-sorted array.

The main inefficiency with this approach is finding the minimum number in the range [`i`, `i + k`] at each index `i`. Linearly searching for it will take O(k) time at each index.

To improve this approach, we'd need a way to efficiently access the minimum value at each of these ranges. A **min-heap** would be perfect for this.

**Min-heap**

For a min-heap to determine the minimum value within each range [`i`, `i + k`], it will always need to be populated with the values in these ranges as we iterate through the array. Let's see how this works over the same example.

---

Before we can determine which value belongs at index 0, we'll need to populate the heap with all the values in the range [0, `k`], which are the first `k + 1` values (where `k = 2` in this example):

![Image represents a step-by-step illustration of a coding pattern, likely involving a min-heap data structure.  The top-l](./images/5240168c_image-08-04-6-J5NWDI3N.svg)

![Image represents a step-by-step illustration of building a min-heap from an array.  The array `[5, 1, 9, 4, 7, 10]` is s](./images/9139e69c_image-08-04-7-6KU6OADY.svg)

![Image represents a snapshot of a step in an algorithm, likely involving a min-heap data structure.  The bottom left show](./images/21e33c9a_image-08-04-8-43QXGWMM.svg)

![Image represents a visual depiction of a step in a sorting algorithm, likely using a min-heap data structure.  The left ](./images/acc7bb27_image-08-04-9-OSCNXPLO.svg)

An alternative way to create a heap of the first `k + 1` elements is to heapify a list of the first `k + 1` elements.

---

Now, let's begin inserting the smallest elements from the heap into the array, using the `insert_index` pointer. The value that belongs at index 0 in sorted order is the value currently at the top of the heap, which is 1:

![The image represents a step in a sorting algorithm, likely using a min-heap data structure.  On the left, a numbered arr](./images/46d62101_image-08-04-10-QJS74Y3J.svg)

Once we insert 1 at index 0, push the value at index `i` to the heap before incrementing both pointers:

![Image represents a step-by-step illustration of building a min-heap from an array.  The top half shows the initial state](./images/8f9f5179_image-08-04-11-VM2M3JGH.svg)

---

Let's continue this process for the remaining numbers:

![Image represents a step-by-step illustration of a sorting algorithm, likely using a min-heap data structure.  The top ha](./images/f9cabc30_image-08-04-12-WJ3JR6OE.svg)

---

![Image represents a visual explanation of a coding pattern, likely involving a min-heap data structure and an array.  The](./images/ca7eef68_image-08-04-13-DI6JAUVJ.svg)

---

![Image represents a visual depiction of inserting an element into a min-heap data structure.  The left side shows an arra](./images/98036750_image-08-04-14-LUFIKKAT.svg)

---

Once there are no more elements to push into the heap, the rest of the array can be sorted by inserting the remaining values from the heap:

![Image represents a step in a sorting algorithm, likely using a min-heap data structure.  The algorithm involves an array](./images/9cd49f84_image-08-04-15-ROEWBFJD.svg)

![Image represents a step in a sorting algorithm, likely heapsort, illustrating the process of inserting elements from a l](./images/af9dcecf_image-08-04-16-VHY33KBY.svg)

![Image represents a step in a sorting algorithm, likely using a min-heap data structure.  The left side shows an array `n](./images/f243b723_image-08-04-17-HIXSCWWN.svg)

![Image represents a visual depiction of a min-heap data structure.  On the left, a green array `[1, 4, 5, 7, 9, 10]` is s](./images/6d30e596_image-08-04-18-DNZHUO7S.svg)

---

Once the heap is empty, the array is sorted.

## Implementation

```python
from typing import List
import heapq
        
def sort_a_k_sorted_array(nums: List[int], k: int) -> List[int]:
    # Populate a min-heap with the first k + 1 values in 'nums'.
    min_heap = nums[:k+1]
    heapq.heapify(min_heap)
    # Replace elements in the array with the minimum from the heap at each
    # iteration.
    insert_index = 0
    for i in range(k + 1, len(nums)):
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
        heapq.heappush(min_heap, nums[i])
    # Pop the remaining elements from the heap to finish sorting the array.
    while min_heap:
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
    return nums

```

```javascript
import { MinPriorityQueue } from './helpers/heap/index.js'

export function sort_a_k_sorted_array(nums, k) {
  // Populate a min-heap with the first k + 1 values in 'nums'.
  const minHeap = new MinPriorityQueue((x) => x)
  for (let i = 0; i <= k && i < nums.length; i++) {
    minHeap.enqueue(nums[i])
  }
  // Replace elements in the array with the minimum from the heap at each iteration.
  let insertIndex = 0
  for (let i = k + 1; i < nums.length; i++) {
    nums[insertIndex] = minHeap.dequeue()
    insertIndex++
    minHeap.enqueue(nums[i])
  }
  // Pop the remaining elements from the heap to finish sorting the array.
  while (!minHeap.isEmpty()) {
    nums[insertIndex] = minHeap.dequeue()
    insertIndex++
  }
  return nums
}

```

```java
import java.util.ArrayList;
import java.util.PriorityQueue;

class Main {
    public ArrayList<Integer> sort_a_k_sorted_array(ArrayList<Integer> nums, int k) {
        // Populate a min-heap with the first k + 1 values in 'nums'.
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int n = nums.size();
        for (int i = 0; i <= Math.min(k, n - 1); i++) {
            minHeap.offer(nums.get(i));
        }
        // Replace elements in the array with the minimum from the heap at each
        // iteration.
        int insertIndex = 0;
        for (int i = k + 1; i < n; i++) {
            nums.set(insertIndex++, minHeap.poll());
            minHeap.offer(nums.get(i));
        }
        // Pop the remaining elements from the heap to finish sorting the array.
        while (!minHeap.isEmpty()) {
            nums.set(insertIndex++, minHeap.poll());
        }
        return nums;
    }
}

```

### Complexity Analysis

**Time complexity:** The time complexity of `sort_a_k_sorted_array` is O(nlog(k)), where n denotes the length of the array. Here's why:

- We perform heapify on a min_heap of size k+1 which takes O(k) time. Note that k is upper-bounded by n in this operation since the heap won't have more than n values.

- Then, we perform `push` and `pop` operations on approximately n-k values using the heap. Since the heap can grow up to a size of k+1, each `push` and `pop` operations takes O(log(k)) time. Therefore, this loop takes O(nlog(k)) time in the worst case.

- The final while-loop runs in O(klog(k)) time since we pop k+1 values from the heap. Note that k here is also upper-bounded by n.

Therefore, the overall time complexity is O(k)+O(nlog(k))+O(klog(k))=O(nlog(k)).

**Space complexity:** The space complexity is O(k) since the heap can grow up to k+1 in size.