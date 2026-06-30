class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack to store opening brackets
        stack = []

        # dictionary for matching closed with open
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        # check each character in the string
        for c in s:
            # if the character is inside the dictionary
            if c in closeToOpen:
                # if closing a bracket
                # check if the stack is not empty and its top matches the opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # pop the stack if yes
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # if the stack is empty, return true
        return True if not stack else False
            