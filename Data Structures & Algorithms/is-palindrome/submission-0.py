class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) -1

        while l < r:

            #skip invalid left and right things
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1

            #main check
            if s[l].lower() != s[r].lower():
                return False
            #increment after each loop
            l, r = l + 1, r - 1
        return True
            
        


