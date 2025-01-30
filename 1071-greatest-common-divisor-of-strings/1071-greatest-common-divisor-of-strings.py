class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Calculate GCD of the lengths of str1 and str2
        len_gcd = gcd(len(str1), len(str2))

        # The potential GCD string
        potential_gcd_str = str1[:len_gcd]

        # Check if the potential GCD string can divide both str1 and str2
        if potential_gcd_str * (len(str1) // len_gcd) == str1 and potential_gcd_str * (len(str2) // len_gcd) == str2:
            return potential_gcd_str
        return ''


