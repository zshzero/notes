class HashTable:
  def __init__(self, size = 11):
    self.data_map = [None] * size

  def __hash(self, key):
    hashValue = 0
    for ch in key:
      hashValue += ord(ch) * 19
    bucket = hashValue % len(self.data_map)
    return bucket 

  def set(self, key, value):
    bucket = self.__hash(key)
    if not self.data_map[bucket]:
      self.data_map[bucket] = []
    self.data_map[bucket].append([key, value])
    return True

  def get(self, key):
    bucket = self.__hash(key)
    if not self.data_map[bucket]:
      return None
    for k,v in self.data_map[bucket]:
      if k == key:
        return [k, v]

  def keys(self):
    keys = []
    for bucket in self.data_map:
      if not bucket:
        continue
      for k,v in bucket:
        keys.append(k)
    return keys

  def print_table(self):
    print()
    print("-----------------------------")
    for i,kv in enumerate(self.data_map):
      print(i, " : ", kv)
    print("-----------------------------")
    print()

ht = HashTable()
ht.print_table()

ht.set("bolts", 500)
ht.set("washers", 100)
ht.set("lumber", 50)
ht.print_table()

print(ht.get("lumber"))
print(ht.get("washers"))
print(ht.get("screws"))

print(ht.keys())

# Interview Question: Check for common elements in given 2 lists

def is_common_elements():
  l1 = [1,2,3]
  l2 = [5,4,3]

  d = {}
  for ele in l1:
    d[ele] = True

  for ele in l2:
    if ele in d:
      return True
  return False

print(is_common_elements())