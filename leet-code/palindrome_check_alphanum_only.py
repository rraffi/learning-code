class Solution:
    # less memory, custom functions
    # def is_palindrome(self, s: str) -> bool:
    #     l, r = 0, len(s) - 1
    #
    #     while l < r:
    #         while l < r and not self.is_alpha_num(s[l]):
    #             l = l+1
    #         while r > l and not self.is_alpha_num(s[r]):
    #             r = r - 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l+1, r-1
    #
    #     return True
    #
    # def is_alpha_num(self, c) -> bool:
    #     return (ord('A') <= ord(c) <= ord('Z') or
    #      ord('a') <= ord(c) <= ord('z') or
    #      ord('0') <= ord(c) <= ord('0'))

    # extra variable & additional memory
    # def is_palindrome(self, s):
    #     new_str = [c.lower() for c in s if c.isalnum()]
    #
    #     l, r = 0, len(new_str)-1
    #
    #     while l < r:
    #         if new_str[l] != new_str[r]:
    #             return False
    #         l, r = l+1, r-1
    #
    #     return True

sol = Solution()
print(sol.is_palindrome("A man, a plan, a canal: Panama"))