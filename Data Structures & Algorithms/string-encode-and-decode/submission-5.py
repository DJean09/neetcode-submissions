class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize an empty result builder
        res = []

        # for each string in the list
        # compute its length
        # append "length#string" to the builder
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        # return the entire list as a joined string
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # initialize an empty list for the decoded strings and pointers i, j = 0
        res = []
        i = 0
        j = 0

        # while i is within the bounds of the encoded string
        while i < len(s):
            # move j forward until it finds # for the length
            while s[j] != '#':
                j += 1
            
            #convert the substring s[i:j] into an integer length
            length = int(s[i:j])

            # move i to the next character after #
            i = j + 1
            # extract the next length characters
            j = i + length
            # append the extracted string to the list
            res.append(s[i:j])

            # move i forward by length to continue
            i = j
        
        # return the decoded list
        return res