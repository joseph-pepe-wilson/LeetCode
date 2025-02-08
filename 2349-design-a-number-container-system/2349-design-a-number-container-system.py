from sortedcontainers import SortedSet


class NumberContainers:
  def __init__(self):
    self.number_to_indices = collections.defaultdict(SortedSet)
    self.index_to_number = {}

  def change(self, index: int, number: int) -> None:
    if index in self.index_to_number:
      original_number = self.index_to_number[index]
      self.number_to_indices[original_number].remove(index)

      if len(self.number_to_indices[original_number]) == 0:
        del self.number_to_indices[original_number]

    self.index_to_number[index] = number
    self.number_to_indices[number].add(index)

  def find(self, number: int) -> int:
    if number in self.number_to_indices:
      return self.number_to_indices[number][0]
    return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)