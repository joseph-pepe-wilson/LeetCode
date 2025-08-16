class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the number to a list of characters (digits)
        num_list = list(str(num))
        
        # Traverse the digits and change the first '6' to '9'
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break  # Only one change allowed
        
        # Convert the list back to an integer
        return int(''.join(num_list))
