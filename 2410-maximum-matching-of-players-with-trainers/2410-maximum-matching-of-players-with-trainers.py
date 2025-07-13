class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort both lists to use two-pointer technique
        players.sort()
        trainers.sort()

        i = j = count = 0

        # Iterate through both lists
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # Match found, move to next player and next trainer
                count += 1
                i += 1
                j += 1
            else:
                # Trainer can't train the current player, try next trainer
                j += 1

        return count
