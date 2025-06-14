class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        # Get the max value by replacing the first non-'9' digit with '9'
        max_digit = next((d for d in num_str if d != '9'), None)
        max_num = int(num_str.replace(max_digit, '9')) if max_digit else num
        
        # Get the min value by replacing the first non-'0' digit with '0'
        min_digit = num_str[0]  # Always replace the first digit for min value
        min_num = int(num_str.replace(min_digit, '0'))
        
        return max_num - min_num
