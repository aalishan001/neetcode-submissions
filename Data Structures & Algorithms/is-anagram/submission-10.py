class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)
        hashmapS = {}
        hashmapT = {}
        for i in range(length):
            hashmapS[s[i]] = hashmapS.get(s[i],0)+1
            hashmapT[t[i]] = hashmapT.get(t[i],0)+1
        if hashmapS == hashmapT:
            return True
        else:
            return False