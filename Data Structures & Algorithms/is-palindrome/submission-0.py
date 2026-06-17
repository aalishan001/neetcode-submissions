class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(char for char in s if char.isalnum())
        a_lower = a.lower()
        if a_lower == a_lower[::-1]:
            return True
        else:
            return False