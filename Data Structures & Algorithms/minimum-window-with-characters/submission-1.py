class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        t_map = {}

        for c in t:
            t_map[c] = t_map.get(c,0) + 1

        left, minWindow = 0, ""

        have, need = 0, len(t_map)
        window_map = {}

        for right in range(len(s)):
            if s[right] in t_map:
                window_map[s[right]] = window_map.get(s[right], 0) + 1
            
                if window_map[s[right]] == t_map[s[right]]:
                    have += 1
                
                while have == need:
                    
                    if not minWindow or len(s[left:right+1]) < len(minWindow):
                        minWindow = s[left:right+1]

                    window_map[s[left]] = window_map.get(s[left],0) - 1

                    if s[left] in t_map and window_map[s[left]] < t_map[s[left]]:
                        have -= 1

                    left += 1


        return minWindow



        




        