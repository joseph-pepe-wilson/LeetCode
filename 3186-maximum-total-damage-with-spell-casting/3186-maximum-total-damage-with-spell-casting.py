from collections import defaultdict
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damage_map = defaultdict(int)
        for p in power:
            damage_map[p] += p  # total damage from all spells with value p

        unique_powers = sorted(damage_map.keys())
        n = len(unique_powers)
        dp = [0] * n

        for i in range(n):
            curr_damage = damage_map[unique_powers[i]]
            # Find the last index j where unique_powers[j] <= unique_powers[i] - 3
            j = i - 1
            while j >= 0 and unique_powers[i] - unique_powers[j] <= 2:
                j -= 1
            if j >= 0:
                dp[i] = max(dp[i - 1], curr_damage + dp[j])
            else:
                dp[i] = max(dp[i - 1], curr_damage)

        return dp[-1]