def bubble_sort(arr: list) -> list:
  for i in range(len(arr)-1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr   

def selection_sort(arr: list) -> list:
  for i in range(len(arr)-1):
    min_i = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[min_i]:
        min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]
  return arr

def insertion_sort(arr: list) -> list:
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j > -1 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr

test_cases = [
    ([5, 3, 6, 2, 10], [2, 3, 5, 6, 10]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([], []),
    ([1], [1]),
    ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),
    ([10, -1, 2, -10, 5], [-10, -1, 2, 5, 10])
]

for input, expected in test_cases:
        assert bubble_sort(input[:]) == expected, f"Failed on input: {input} with bubble_sort"
        assert selection_sort(input[:]) == expected, f"Failed on input: {input} with selection_sort"