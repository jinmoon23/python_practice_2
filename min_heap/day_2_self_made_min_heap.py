class MinHeap:
  def __init__(self):
    self.items = []
  
  def size(self):
    return len(self.items)
  
  def push(self, item):
    self.items.append(item)
    self.bubble_up()
  
  def pop(self):
    min = self.items[0]
    self.items[0] = self.items[self.size() - 1]
    self.items.pop()
    self.bubble_down()
    return min
  
  def swap(self, a, b):
    self.items[a], self.items[b] = self.items[b], self.items[a]

  def bubble_up(self):
    index = self.size() - 1
    while index > 0:
      parent_index = (index - 1) // 2
      if self.items[parent_index] <= self.items[index]: break
      self.swap(parent_index, index)
      index = parent_index
  
  def bubble_down(self):
    index = 0
    while index * 2 + 1 < self.size():
      left_child, right_child = index * 2 + 1, index * 2 + 2
      smaller_child = left_child
      if right_child < self.size() and self.items[right_child] < self.items[left_child]: smaller_child = right_child
      if self.items[index] <= self.items[smaller_child]: break
      self.swap(smaller_child, index)
      index = smaller_child

heap = MinHeap()
for i in [5,3,10,1]:
  heap.push(i)

print(heap.items)
print(heap.pop())
print(heap.items)
print(heap.pop())