class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Determine max value (replace first non-9 digit with 9)
        max_digit = next((d for d in s if d != '9'), None)
        max_value = int(s.replace(max_digit, '9')) if max_digit else num

        # Determine min value (replace first digit if >1, otherwise replace first non-0/1 digit with 0)
        min_digit = s[0] if s[0] > '1' else next((d for d in s if d not in {'0', '1'}), None)
        min_value = int(s.replace(min_digit, '0' if s[0] == '1' else '1')) if min_digit else num

        return max_value - min_value
