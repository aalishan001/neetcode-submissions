class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        arr = []
        for num , cnt in count.items():
            arr.append([cnt,num])
        print(arr)
        arr.sort()
        print(arr)
        res=[]
        while len(res)<k:
            print(res)
            res.append(arr.pop()[1])
            print(res)
        return res