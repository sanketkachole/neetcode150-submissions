class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False 


        stack_LIFO = []
        string_dictionary = {
                    "(":")", 
                    "[":"]", 
                    "{":"}"
                    }

        for string in s:
            if string in string_dictionary:
                stack_LIFO.append(string)
            else:
                if not stack_LIFO:
                    return False
                elif string == string_dictionary[stack_LIFO[-1]]:
                    stack_LIFO.pop()
                else:
                    
                    return False
                    
        return not stack_LIFO			
            