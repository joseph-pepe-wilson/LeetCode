from sortedcontainers import SortedDict, SortedSet
class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_index = collections.defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        # If the index already exists in index_to_number, remove the old number from number_to_index
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_index[old_number].remove(index)
            if not self.number_to_index[old_number]:
                del self.number_to_index[old_number]

        self.index_to_number[index] = number # Update the index_to_number dictionary

        if number not in self.number_to_index:
            self.number_to_index[number] = set()
        self.number_to_index[number].add(index) # Add the index to the number_to_index dictionary

    def find(self, number: int) -> int:
        # If the number is in the number_to_index dictionary, return the smallest index
        if number in self.number_to_index and self.number_to_index[number]:
            return min(self.number_to_index[number])
        else:
            return -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)