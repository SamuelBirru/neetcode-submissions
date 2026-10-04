from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = sorted(s)
            res[tuple(sorted_s)].append(s)


        for val in res.values():
            result.append(val) 

        return result       
        """
        list of strings

        """


        
        