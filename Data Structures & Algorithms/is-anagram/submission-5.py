class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        listS = list(s)
        listT = list(t)
        for i in listS:
            if i in listT:
                listT.remove(i)
            else:
                return False
        return True
        