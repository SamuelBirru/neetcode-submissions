class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for let in s:
            if let not in dict1:
                dict1[let] = 1
            else:
                dict1[let] += 1
        
        for let in t:
            if let not in dict2:
                dict2[let] = 1
            else:
                dict2[let] += 1

        return dict1 == dict2