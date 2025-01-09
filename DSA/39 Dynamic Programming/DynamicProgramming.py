counter = 0
def r_fib(n: int) -> int:
  global counter 
  counter += 1
  if n == 0 or n == 1:
    return n
  return r_fib(n-1) + r_fib(n-2)
print(r_fib(30), counter) # 832040 2692537

counter = 0
memo = [None] * 100
def r_memo_fib(n: int) -> int:
  global counter 
  counter += 1
  if memo[n]:
    return memo[n]
  if n == 0 or n == 1:
    return n
  memo[n] = r_memo_fib(n-1) + r_memo_fib(n-2)
  return memo[n]
print(r_memo_fib(30), counter) # 832040 59

counter = 0
def itr_fib(n: int) -> int:
  fib_store = [0, 1]
  global counter
  for i in range(2, n+1):
    counter += 1
    fib_next = fib_store[i-1] + fib_store[i-2]
    fib_store.append(fib_next)
  return fib_store[n]
print(itr_fib(30), counter) # 832040 29