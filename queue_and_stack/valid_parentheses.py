class Solution:
    def isValid(self, s: str) -> bool:
        stack, my_set1, my_set2 = [], set("({["), set(")}]")
        for c in s:
            if c in my_set1:
                stack.append(c)
            if c in my_set2:
                if not stack:
                    return False 
                else:
                    top_c = stack.pop()
                    if c == ')':
                        if top_c != '(':
                            return False 
                    elif c == ']':
                        if top_c != '[':
                            return False
                    elif c == '}':
                        if top_c != '{':
                            return False 
        return not stack