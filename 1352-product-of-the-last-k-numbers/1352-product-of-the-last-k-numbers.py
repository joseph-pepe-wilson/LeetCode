class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1] # Initialize with 1 to handle multiplication

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1] # If num is 0, reset the prefix_products list
        else:
            self.prefix_products.append(self.prefix_products[-1] * num) # Append the product of the new num with the last prefix product

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0
        return self.prefix_products[-1] // self.prefix_products[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)