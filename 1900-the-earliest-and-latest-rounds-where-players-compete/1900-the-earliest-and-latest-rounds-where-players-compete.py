class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(players: tuple, round_num: int) -> tuple:
            if firstPlayer in players and secondPlayer in players:
                i, j = players.index(firstPlayer), players.index(secondPlayer)
                if i + j == len(players) - 1:
                    return round_num, round_num

            next_rounds = set()
            l = 0
            r = len(players) - 1

            while l < r:
                matchups = []

                # Handle each match in current round
                while l < r:
                    p1, p2 = players[l], players[r]

                    if {p1, p2} == {firstPlayer, secondPlayer}:
                        pass  # Already handled earlier
                    elif p1 in (firstPlayer, secondPlayer):
                        matchups.append(p1)
                    elif p2 in (firstPlayer, secondPlayer):
                        matchups.append(p2)
                    else:
                        matchups.append((p1, p2))  # Both are regulars
                    l += 1
                    r -= 1

                if l == r:
                    matchups.append(players[l])  # odd count case

                # Process all possible outcomes for non-key matches
                def backtrack(i, current):
                    if i == len(matchups):
                        res = dfs(tuple(sorted(current)), round_num + 1)
                        next_rounds.add(res)
                        return
                    match = matchups[i]
                    if isinstance(match, int):
                        backtrack(i + 1, current + [match])
                    else:
                        backtrack(i + 1, current + [match[0]])
                        backtrack(i + 1, current + [match[1]])

                backtrack(0, [])

            return min(x[0] for x in next_rounds), max(x[1] for x in next_rounds)

        initial = tuple(range(1, n + 1))
        return list(dfs(initial, 1))
