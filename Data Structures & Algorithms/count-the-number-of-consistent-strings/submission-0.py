class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        need = {}
        count = 0
        for n in allowed:
            need[n] = None


        for word in words:
            same = True
            for letter in word:
                if letter not in need:
                    same = False

                
            if same:
                count += 1

            
        return count


        