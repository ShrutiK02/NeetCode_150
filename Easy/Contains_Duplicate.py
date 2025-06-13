#
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for number in nums:
            if number in d:
                return True
            d[number] = 1
        return False