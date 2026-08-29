class Solution:
    def isValid(self, s: str) -> bool:

        l = []
        for i in s:
            if i == "(":
                l.append(')')
            elif i=='{' : 
                l.append('}')
            elif i=='[':
                l.append(']')
            else:
                if len(l)==0:
                    return False
                else:
                    if l.pop()!=i:
                        return False
        if len(l)>0:
            return False
        return True
                
        