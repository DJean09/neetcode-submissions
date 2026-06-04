class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use defaultdict(list) for grouping, counting, or appending
        anaHash = defaultdict(list)

        for word in strs:
            # sort then use "".join() to join the sorted list
            key = "".join(sorted(word))

            # Because of defaultdict(list), we can append the word
            # without worry of the key existing
            anaHash[key].append(word)

        # use list to receive values as a tuple
        return list(anaHash.values())
