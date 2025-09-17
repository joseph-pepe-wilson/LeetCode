from typing import List
import heapq

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_data = {}  # food -> [cuisine, rating]
        self.cuisine_heaps = {}  # cuisine -> heap of (-rating, food)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_data[food] = [cuisine, rating]
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, old_rating = self.food_data[food]
        self.food_data[food][1] = newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating, food = heap[0]
            current_rating = self.food_data[food][1]
            if -rating == current_rating:
                return food
            else:
                heapq.heappop(heap)
        return ""
