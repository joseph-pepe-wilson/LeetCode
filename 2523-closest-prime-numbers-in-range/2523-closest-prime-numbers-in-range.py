from typing import List

class Solution:
    def is_prime(self, n: int):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [i for i in range(left, right + 1) if self.is_prime(i)]
        if len(prime) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(prime) - 1):
            diff = prime[i + 1] - prime[i]
            if diff < min_diff:
                min_diff =diff
                ans = [prime[i], prime[i + 1]]

        return ans