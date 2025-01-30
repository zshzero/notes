# Hash Table Interview LeetCode Exercises

### [0. HT Item In Common]()

```py
# Dict
# Time Complexity - O(n + m)
# Space Complexity - O(n)
def item_in_common(self, list1: List[int], list2: List[int]) -> bool:
    # initialize dict for lookup convenience
    d = {}

    # traverse list1 and add it to d
    for i in list1:
        d[i] = True

    # traverse list2 and check if it exist in d
    for j in list2:
        if j in d:
            return True

    return False
```

### [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array)

```py
# HashSet
# Time Complexity - O(n)
# Space Complexity - O(n)
  def findDuplicates(self, nums: List[int]) -> List[int]:
      # initialize set and dups list
      s = set()
      dups = []

      # for every num in nums, add it to dups 
      # if its in set else add it to set
      for num in nums:
          if num in s:
              dups.append(num)
          else:
              s.add(num)
      return dups
```

```py
# Array Manipulation (works only coz the values are in range [1, n])
# Time Complexity - O(n)
# Space Complexity - O(n)
def findDuplicates(self, nums: List[int]) -> List[int]:
    # initialize array with nums length and dups list
    arr = [0] * len(nums)
    dups = []

    # for every num in nums, add it to dups 
    # if its in arr else add it to arr
    for num in nums:
        if arr[num - 1] == 1:
            dups.append(num)
        else:
            arr[num - 1] = 1
    return dups
```

```py
# Mark visited val (works only coz the values are in range [1, n])
# Time Complexity - O(n)
# Space Complexity - O(1)
def findDuplicates(self, nums: List[int]) -> List[int]:
    # initialize dups list
    dups = []
    
    # for every num in nums, check if if val is neg and visited 
    for n in nums:
        # get original val
        n = abs(n)
        if nums[n-1] > 0:
            nums[n-1] = -nums[n-1]
        else:
            dups.append(n)
    return dups
```

### [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string)

```py
# Dict or Hash Table + BruteForce
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(n) => O(1) as its 26 chars always
def firstUniqChar(self, s: str) -> int:
    # initialize dict to store count
    d = {}

    # traverse str and count occurrences
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1

    # enumerate str and check for one occurrence
    for i,ch in enumerate(s):
        # print(i,ch)
        if d[ch] == 1:
            return i
    return -1
```

```py
# Array Manipulation
# Time Complexity - O(n + n) => O(n)
# Space Complexity - O(26) => O(1)
def firstUniqChar(self, s: str) -> int:
    # initialize arr for 26 chars
    freq = [0] * 26
    # compute ascii of 'a' once
    ordA = ord('a')

    # traverse str and update count in their resp. index
    for c in s:
        freq[ord(c)-ordA] += 1

    # enumerate str and check for one occurrence 
    for i,c in enumerate(s):
        if freq[ord(c)-ordA] == 1:
            return i
    return -1
```

### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

```py
# Sort string chars + Dict or Hash Table (n = no. of str in strs and k = max len of a str)
# Time Complexity - O(n(loop) * (k logk (sorting) + k (joining)) 
#                     + O(m)) => O(n * klogk + O(m)) => O(n*klogk)
# Space Complexity - O(n * k)

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # initialize dict to store 
    # sorted string as key and strs as values
    d = {}

    # traverse strs, sort the chars and add them to resp. list
    for s in strs:
        sortedS = ''.join(sorted(s))
        # print(sortedS)
        if sortedS in d:
            d[sortedS].append(s)
        else:
            d[sortedS] = [s]

    # convert them to list and return
    return list(d.values())
```

```py
# String Freq + Dict or Hash Table (n = no. of str in strs and k = max len of a str)
# Time Complexity - O(n * k) + O(m)(converting dict values to list)) => O(n*k)
# Space Complexity - O(n * k)(d) + O(1)(freq) + O(1)(tuple(freq)) 
#                    + O(n)(list(d.values())) => O(n * m)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # initialize dict to store 
    # freq arr as key and strs as values
    d = {}
    # compute ascii of 'a' once
    ordA = ord('a')

    # traverse strs, sort the chars and add them to resp. list
    for s in strs:
        # arr to hold freq of chars in string
        freq = [0] * 26
        for ch in s:
            # convert them to ascii and view them as arr index
            index = ord(ch) - ordA
            freq[index] += 1
        # list can't be hashed. use tuple conversion
        if tuple(freq) in d:
            d[tuple(freq)].append(s)
        else:
            d[tuple(freq)] = [s]

    # convert them to list and return
    return list(d.values())
```

### [1. Two Sum](https://leetcode.com/problems/two-sum)

```py
# Brute Force
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # traverse all ele to calculate sum
    for i in range(len(nums)):
        # traverse from next ele to calculate sum
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
```

```py
# Dict or Hash Table
# Time Complexity - O(n)
# Space Complexity - O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # initialize dict to store num and its index
    d = {}

    # traverse nums and calculate diff with target 
    for i in range(len(nums)):
        diff = target - nums[i]
        # check if diff existed in dict else add num, index to dict
        if diff in d:
            return [i,d[diff]]
        else:
            d[nums[i]] = i
```

### [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k)

```py
# Brute Force
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def subarraySum(self, nums: List[int], k: int) -> int:
    # initialize count to keep track of sum which equals k 
    count = 0

    # traverse all ele to calculate sum
    for i in range(len(nums)):
        # initialize sum with i^th num and check if it equals k
        sum = nums[i]
        if sum == k: count += 1
        # add j^th num and check if it equals k
        for j in range(i+1,len(nums)):
            sum += nums[j]
            if sum == k: count += 1
    return count
```

```py
# Dict or Hash Table + Prefix Sum
# Time Complexity - O(n * n) => O(n^2)
# Space Complexity - O(1)
def subarraySum(self, nums: List[int], k: int) -> int:
    # initialize count to keep track of sum which equals k,
    # prefixSum to hold sum until curr ele and
    # dict to store prefixSum and count of it
    count = 0
    prefixSum = 0
    d = { 0: 1}

     # traverse all ele
    for num in nums:
        # calculate sum till point
        prefixSum += num
        # calculate diff that needs to be removed to get k 
        remove = prefixSum - k
        # check if its present in dict, add it value to count
        # dict with key diff will give count of occurrences 
        if remove in d:
            count += d[remove]
        # update dict with prefix or incr if it already exists
        d[prefixSum] = 1 + d.get(prefixSum,0)
    return count
```

### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

```py
# Two pointer
# Time Complexity - O(n)
# Space Complexity - O(1)
def removeDuplicates(self, nums: List[int]) -> int:
    # initialize left ptr
    # add dummy node at end (-101 is based on nums[i] constraint)
    left = 0
    nums.append(-101)

    # traverse nums, compare previous and curr ele
    # if not equal, then update value and left ptr
    for right in range(1, len(nums)):
        # first unique number in dup sequence
        if nums[right-1] != nums[right]:
            nums[left] = nums[right-1]
            left += 1
            
    # left is till where list should be checked
    return left
```

### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate)

```py
# Set
# Time Complexity - O(n)
# Space Complexity - O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False
```

```py
# Dict
# Time Complexity - O(n)
# Space Complexity - O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    # initialize dict for lookup convenience
    d = {}

    # traverse nums and return if its already in set else add it
    for num in nums:
        if num in d:
            return True
        d[num] = 1
    return False
```

### [0. Set Find Pairs]()

```py
# Set
# Time Complexity - O(n + m)
# Space Complexity - O(n + m)
def find_pairs(arr1: List[int], arr2: List[int], target: int) -> List[Tuple[int, int]]:
    # initialize set for lookup convenience
    s = set(arr1)
    pairs = []

    # traverse arr2, calculate diff and see if it exist in set 
    for num in arr2:
        diff = target - num
        if diff in s:
            pairs.append((diff, num))

    return pairs
```

### [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)

```py
# Set + Sequence Check
# Time Complexity - O(n*logn + n) => O(n*logn)
# Space Complexity - O(n)
def longestConsecutive(self, nums: List[int]) -> int:
    # sort list to bring consecutive ele together
    sortedNums = sorted(nums)
    # initialize previous ele to negative infinity for comparison
    prev = -inf
    # initialize length of curr sequence and longest sequence
    currLength = 0
    longest = 0

    # traverse sorted list to find longest consecutive sequence
    for num in sorted_nums:
        # if curr extends sequence, incr curr length
        if num - 1 == prev:
            curr_length += 1
        # if curr is not part of sequence, reset curr len
        elif prev != num:
            curr_length = 1
        
        # update prev to current ele
        prev = num
        # update longest sequence length if current one is longer
        longest = max(longest, curr_length)
    
    return longest
```

```py
# Set + Sequence Check
# Time Complexity - O(n(set) + n(for) + n(while)) => O(n)
    # while loop's worst-case scenario seems O(n), 
    # but doesn't apply to every ele individually across all passes.
    # while loop only runs for beginning of each sequence
# Space Complexity - O(n)
def longestConsecutive(self, nums: List[int]) -> int:
    # initialize set for lookup convenience and
    # longest to keep track of sequence
    s = set(nums)
    longest = 0

    # traverse nums, check if it has a left ele
    for num in nums:
        if num - 1 in s:
            continue
        # update sequence len by checking next ele
        currLength = 0
        while num + currLength in s:
            currLength += 1
        # check if curr sequence len is longer than previous
        longest = max(longest, currLength)
    
    return longest
```