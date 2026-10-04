class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            dictionary[sortedWord].append(word)
        
        return list(dictionary.values())
