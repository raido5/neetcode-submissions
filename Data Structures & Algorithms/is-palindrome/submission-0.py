class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ss=""
        for i in s:
            if i.isalnum():
                ss+=i.lower()
        l=0
        r=len(ss)-1
        while l<r:
            if ss[l]!=ss[r]:
                print(ss[l])
                print(ss[r])
                return False
            l+=1
            r-=1
        return True