class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False



        dic1 = [0]*26
        dic2 = [0]*26
        for i in range(len(s1)):
            dic1[ord(s1[i])-ord('a')]+= 1
        
        for i in range(len(s2)):
            if i>=len(s1):
                dic2[ord(s2[i-len(s1)])-ord('a')]-= 1
            dic2[ord(s2[i])-ord('a')]+= 1

            if dic1==dic2:
                return True
        return False

            



        

    

        