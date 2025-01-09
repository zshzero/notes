def pivot(l: list, pivot_index: int, end_index: int) -> int:
  swap = pivot_index
  for i in range(pivot_index+1, end_index+1):
    if l[i] < l[pivot_index]:
      swap += 1
      l[swap], l[i] = l[i], l[swap]
  l[pivot_index], l[swap] = l[swap], l[pivot_index]
  return swap

assert pivot([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 0, 9) == 3
assert pivot([1, 2, 3, 4, 5], 0, 4) == 0
assert pivot([5, 4, 3, 2, 1], 0, 4) == 4
assert pivot([1, 2, 3, 4, 0], 0, 4) == 1
assert pivot([0, 2, 3, 4, 1], 0, 4) == 0

def __r_quick_sort(l: list, le: int, ri: int) -> list:
  if le < ri:
    pivot_index = pivot(l, le, ri)
    __r_quick_sort(l, le, pivot_index-1)
    __r_quick_sort(l, pivot_index+1, ri)
  return l

def quick_sort(l: list) -> list:
  return __r_quick_sort(l, 0, len(l)-1)

assert quick_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert quick_sort([]) == []
assert quick_sort([1]) == [1]
assert quick_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert quick_sort([10, -1, 2, -10, 5]) == [-10, -1, 2, 5, 10]
