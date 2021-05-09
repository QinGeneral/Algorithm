class Solution:
    def countBits(self, num: int) -> List[int]:

        result = []
        for i in range(num + 1):
            result.append(self.hammingWeight(i))
        return result

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            result.append(result[i & (i - 1)] + 1)
        return result