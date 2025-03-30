class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Find the last occurrence of each character in the string
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        # Initialize the result list and variables to track the start and end of a partition
        result = []
        start, end = 0, 0
        
        # Iterate through the string to determine partitions
        for i, char in enumerate(s):
            # Update the end of the current partition to the maximum last occurrence of the character
            end = max(end, last_occurrence[char])
            
            # If the current index matches the end of the partition
            if i == end:
                # Add the size of the partition to the result
                result.append(end - start + 1)
                # Move the start to the next character
                start = i + 1
        
        return result
