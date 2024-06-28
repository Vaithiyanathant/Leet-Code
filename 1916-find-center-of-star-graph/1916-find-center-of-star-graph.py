class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(int)
        for i,j in edges:
            d[i]+=1
            d[j]+=1
        maxi = max(d.values())
        for i,j in d.items():
            if j==maxi:
                return i
        return -1
        

        