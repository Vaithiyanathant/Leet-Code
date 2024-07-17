class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        def check(ind,target):
            if ind == len(candidates):
                if target == 0 :
                    ans.append(ds[:])
                return
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                check(ind,target-candidates[ind])
                ds.pop()
            check(ind+1,target)

        check(0,target)
        return ans
