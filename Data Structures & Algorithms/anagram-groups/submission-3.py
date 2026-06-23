class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaHash = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anaHash[key].append(word)
        
        return list(anaHash.values())