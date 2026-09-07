class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        ss = [0]*26
        tt = [0]*26

        for i in range(len(s)):
            ss[ord(s[i])-ord('a')]+=1
        for i in range(len(s)):
            tt[ord(t[i])-ord('a')]+=1

        if ss!=tt:return False
        return True
