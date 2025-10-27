class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        # Count devices in each row, ignore empty rows.
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]
        
        total_beams = 0
        # Iterate over consecutive rows with devices.
        for i in range(1, len(device_counts)):
            # Multiply the count of adjacent non-empty rows.
            total_beams += device_counts[i - 1] * device_counts[i]
        return total_beams
