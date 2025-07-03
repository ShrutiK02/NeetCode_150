class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = s.strip()
        length_s = len(test)
        for i in range(length_s//2):
            j = (length_s - 1) - i
            if test[i] != test[j]:
                return False
        return True
        