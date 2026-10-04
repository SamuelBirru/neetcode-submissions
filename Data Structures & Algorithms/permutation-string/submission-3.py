class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)
        if k > n:
            return False

        # need: counts of s1
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        # window: counts in current window of s2
        window = {}
        for i in range(k):
            c = s2[i]
            window[c] = window.get(c, 0) + 1

        if window == need:
            return True

        # slide the window
        for r in range(k, n):
            add = s2[r]
            rem = s2[r - k]

            window[add] = window.get(add, 0) + 1

            window[rem] -= 1
            if window[rem] == 0:
                del window[rem]  # keep dict small and equality cheap

            if window == need:
                return True

        return False

