# Heap Interview LeetCode Exercises

### [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

```py
# Heap
# Time Complexity - O(n*logn) + O((k-1)*logn) => O(n*logn)
# Space Complexity - O(n)
def findKthLargest(self, nums: List[int], k: int) -> int:
    def left_index(index):
        return index * 2 + 1
    
    def right_index(index):
        return index * 2 + 2
    
    def parent_index(index):
        return (index-1) // 2
    
    # When there are no nodes, Return None
    if len(nums) == 0:
        return None

    # When there is one node, Pop and return it
    if len(nums) == 1:
        return nums.pop()

    # Initializing heap list
    heap = []

    # Heapifying the list
    for num in nums:
        heap.append(num)

        curr = len(heap) - 1
        while curr > 0 and heap[parent_index(curr)] < heap[curr]:
            heap[parent_index(curr)], heap[curr] = heap[curr], heap[parent_index(curr)]
            curr = parent_index(curr)
    # print(heap)

    # Popping the nodes k-1 times
    for _ in range(k - 1):
        heap[0] = heap.pop()

        curr = 0
        max_ptr = 0
        while True:
            left = left_index(curr)
            right = right_index(curr)

            if left < len(heap) and heap[left] > heap[max_ptr]:
                max_ptr = left

            if right < len(heap) and heap[right] > heap[max_ptr]:
                max_ptr = right

            if curr != max_ptr:
                heap[curr], heap[max_ptr] = heap[max_ptr], heap[curr]
                curr = max_ptr
            else:
                break

    # return the kth largest 
    return heap[0]
```

```py
# Heap using module
# Time Complexity - O(n) + O((n-k)*log(n))
# Space Complexity - O(1)
def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return nums[0]
```

```py
# Quick Select
# Time Complexity - O(n+ n/2 + n/4 ...) => O(2n) => O(n)
# Space Complexity - O(1)
def findKthLargest(self, nums: List[int], k: int) -> int:
    # calculate index of kth ele
    kIndex = len(nums) - k
    
    def quickSelect(l: int, r: int) -> int:
        # Include below snippet to randomize pivot index
        # pivot_index = random.randint(l, r)
        # nums[pivot_index], nums[r] = nums[r], nums[pivot_index]

        # initialize ptr to determine pivot's sort position
        # and pivot ele to move to its sort position 
        ptr, pivot = l, nums[r]

        # traverse from left to right
        for i in range(l,r):
            # if pivot is greater than curr, swap ptr and curr ele, incr ptr
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]  
                ptr += 1
        # swap ptr and right ele 
        nums[ptr], nums[r] = nums[r], nums[ptr]

        # select again if kth ele lies in right partition
        if ptr < kIndex:
            return quickSelect(ptr+1, r)
        # select again if kth ele lies in left partition
        elif ptr > kIndex:
            return quickSelect(l, ptr-1)
        # found kth ele 
        else:
            return nums[ptr]

    return quickSelect(0, len(nums) - 1)
```

### [0. Heap Maximum Element in a Stream]()

```py
# BruteForce
# Time Complexity - O(n)
# Space Complexity - O(1)
def stream_max(nums):
    if not nums: 
        return nums
    
    # initialize max_val to keep track of max val
    max_val = nums[0]
    # traverse nums
    for i in range(len(nums)):
        # compare and update max val if they are greater
        if max_val <= nums[i]:
              max_val = nums[i]
        # overwrite with max val
        nums[i] = max_val
    
    return nums
```

```py
# BruteForce using heap
# Time Complexity - O(n * logn)
# Space Complexity - O(n)
def stream_max(nums):
     # initialize max_heap to heapify nums
     # and max_stream to store updated values
    max_heap = MaxHeap()
    max_stream = []

    # traverse nums
    for num in nums:
        # insert num and max is pushed to top (heap property)
        max_heap.insert(num)
        # add max val to max stream
        max_stream.append(max_heap.heap[0])

    return max_stream
```