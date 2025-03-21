from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create a graph and in-degree tracker
        ingredient_to_recipe = defaultdict(list)
        in_degree = defaultdict(int)
        
        # Build the graph
        for recipe, required_ingredients in zip(recipes, ingredients):
            for ingredient in required_ingredients:
                ingredient_to_recipe[ingredient].append(recipe)
            in_degree[recipe] += len(required_ingredients)
        
        # Initialize queue with supplies
        queue = deque(supplies)
        result = []
        
        # Perform topological sort
        while queue:
            current_ingredient = queue.popleft()
            
            if current_ingredient in recipes:
                result.append(current_ingredient)
            
            for recipe in ingredient_to_recipe[current_ingredient]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    queue.append(recipe)
        
        return result
