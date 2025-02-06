class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = {}
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product in product_count:
                    count += product_count[product]
                    product_count[product] += 1
                else:
                    product_count[product] = 1

        return count * 8