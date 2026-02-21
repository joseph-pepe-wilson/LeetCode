primes = [0] * 32

for i in range(2,32):
    j = i + i
    while j < 32:
        primes[j] = i
        j += i



class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def condition(num):
            count = 0

            while num:
                num = num & (num - 1)
                count += 1
            
            return primes[count] == 0 and (count >= 2)
        


        answer = 0

        for num in range(left, right + 1):
            answer += condition(num)
        return answer