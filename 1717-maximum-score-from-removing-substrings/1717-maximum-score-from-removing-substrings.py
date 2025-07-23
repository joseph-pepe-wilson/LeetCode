class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(string: str, target: str) -> tuple[str, int]:
            # We convert string to list because in this language strings are immutable and so complexity is still O(n) but in languages where strings are mutable this will be O(1)
            string = list(string)
            write_ind = 0
            counting = 0

            for char in string:
                string[write_ind] = char
                write_ind += 1

                if write_ind >= 2:
                    if string[write_ind - 1] == target[1] and string[write_ind - 2] == target[0]:
                        counting += 1
                        write_ind -= 2

            return ("".join(string[:write_ind]), counting)

        result = 0
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        remainder, c = remove_pairs(s, top)
        result += c * top_score
        _, c = remove_pairs(remainder, bot)
        result += c * bot_score

        return result
