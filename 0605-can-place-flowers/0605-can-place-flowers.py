class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            # Check if the current plot is empty and adjacent plots are also empty or out of bounds
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                # Plant a flower
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False