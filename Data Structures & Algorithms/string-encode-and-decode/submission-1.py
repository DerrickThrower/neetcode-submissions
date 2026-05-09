class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""

        if not strs:
            return ""
        
        for word in strs:

            coded += str(len(word)) + "#" + word

        return coded
            

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":

                j+= 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j

        return decoded







