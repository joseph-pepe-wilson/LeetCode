class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle negative numbers
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        
        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        # If no remainder, return as integer
        if remainder == 0:
            return ''.join(result)
        
        result.append('.')
        # Dictionary to store previously seen remainders and their index
        rem_pos = {}
        
        while remainder != 0:
            if remainder in rem_pos:
                # Repeating part found
                idx = rem_pos[remainder]
                result.insert(idx, '(')
                result.append(')')
                break
            rem_pos[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(result)
