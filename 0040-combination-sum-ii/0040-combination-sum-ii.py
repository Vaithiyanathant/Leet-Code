class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ds = [ ]
        ans =[ ]
        c = sorted(candidates)
        def combi(ind,tar):
            if tar == 0 :
                ans.append(ds[:])
                return 
            for i in range(ind,len(c)):
                if i>ind and c[i]==c[i-1]: 
                    continue 
                if c[i]>tar:
                    break
                ds.append(c[i])
                combi(i+1,tar-c[i])  
                ds.pop()

        combi(0,target)
        return ans    