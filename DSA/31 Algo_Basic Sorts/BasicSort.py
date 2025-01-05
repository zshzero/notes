def bubble_sort(l: list) -> list:
  for i in range(len(l)-1, 0, -1):
    for j in range(i):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]
  return l

assert bubble_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort([]) == []
assert bubble_sort([1]) == [1]
assert bubble_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert bubble_sort([10, -1, 2, -10, 5]) == [-10, -1, 2, 5, 10]

def selection_sort(l: list) -> list:
  for i in range(len(l)-1):
    min_index = i
    for j in range(i+1, len(l)):
      if l[min_index] > l[j]:
        min_index = j
    l[i], l[min_index] = l[min_index], l[i]
  return l

assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert selection_sort([]) == []
assert selection_sort([1]) == [1]
assert selection_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert selection_sort([10, -1, 2, -10, 5]) == [-10, -1, 2, 5, 10]

def insertion_sort(l: list) -> list:
  for i in range(1, len(l)):
    key = l[i]
    j = i - 1
    while j > -1 and l[j] > key:
      l[j+1] = l[j]
      j -= 1
    l[j+1] = key
  return l

assert insertion_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert insertion_sort([]) == []
assert insertion_sort([1]) == [1]
assert insertion_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert insertion_sort([10, -1, 2, -10, 5]) == [-10, -1, 2, 5, 10]
