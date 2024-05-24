class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def sol(i,n,temp,arr):
            if i == n:
                out.append(temp[:])
                return 
            temp.append(arr[i])
            sol(i+1,n,temp,arr)
            temp.pop()
            sol(i+1,n,temp,arr)
        ind = 0
        n = len(nums)
        y = []
        
        sol(ind,n,y,nums)
        return out

        
