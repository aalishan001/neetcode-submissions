class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                idx = ord(ch)-ord("a")
                count[idx] += 1
            hashes[tuple(count)].append(s)
        return list(hashes.values())