class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #slide through s2 with a fixed window of s1
        # if a window contains the same set of letters .split() then set them



        
        l , r = 0, len(s1)
        hash1 = {}

        for char in s1:

            hash1[char] = s1.count(char)


        while r <= len(s2):

            stringchecking = s2[l:r]
            hash2 = {}
            
            for char in stringchecking:

                hash2[char] = stringchecking.count(char)

            if hash2 == hash1:
                return True

        
            else:
                l+=1
                r+=1

        return False

