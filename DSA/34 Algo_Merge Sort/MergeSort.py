def merge(l1: list, l2: list) -> list:
  result = []
  i, j = 0, 0
  while i < len(l1) and j < len(l2):
      if l1[i] < l2[j]:
        result.append(l1[i])
        i += 1
      else:
        result.append(l2[j])
        j += 1
  while i < len(l1):
    result.append(l1[i])
    i += 1
  while j < len(l2):
    result.append(l2[j])
    j += 1

  return result

assert merge([2,5,7], [1,4,6]) == [1,2,4,5,6,7]
assert merge([1,2,7,8], [3,4,5,6]) == [1,2,3,4,5,6,7,8]
assert merge([],[]) == []
assert merge([1], [2]) == [1,2]

def merge_sort(l: list) -> list:
  if len(l) <= 1:
    return l
  mid = len(l) // 2
  l1 = merge_sort(l[:mid])
  l2 = merge_sort(l[mid:])
  return merge(l1,l2)

assert merge_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert merge_sort([10, -1, 2, -10, 5]) == [-10, -1, 2, 5, 10]
