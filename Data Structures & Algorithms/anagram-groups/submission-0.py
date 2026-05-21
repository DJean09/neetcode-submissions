class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Automatically create default values
        # Best for grouping, counting, or appending data
        strHash = defaultdict(list)

        # Search through each word
        for s in strs:
            # Use sorted() to sort the characters
            # Use "".join() to put the sorted list into a string
            key = "".join(sorted(s))
            # Append the word into the key
            # All anagrams will have the same Key
            strHash[key].append(s)
        
        # Use list() to receive the values as a tuple
        return list(strHash.values())