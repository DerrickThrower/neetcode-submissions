class Solution:
    def validPalindrome(self, s: str) -> bool:

        def valid(x):

            l, r = 0, len(x)- 1

            while l < r:
                if x[l] != x[r]:
                    return False

                l+=1
                r -=1

            return True

        
        l, r = 0, len(s) -1

        while l < r:
            if s[l] != s[r]:
                return valid(s[l+1:r+1]) or valid(s[l:r])

            l +=1
            r -= 1

        return True
