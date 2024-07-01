class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = groupSizes 
        f = {}
        for i in range(len(g)):
            if g[i] not in f:
                f[g[i]] = []
            f[g[i]].append(i)
        print(f)
        res =[ ]
        for key,value in f.items():
            for i in range(0,len(value),key):
                res.append(value[i:i+key])
        return res



        return ans

        