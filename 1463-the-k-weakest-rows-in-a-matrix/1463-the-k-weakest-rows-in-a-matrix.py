class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def check(row):
            low =  0
            high = len(row)-1
            res = -1
            while(low<=high):
                mid = (low+high)//2
                if row[mid]==1:
                    res = mid
                    low = mid+1
                elif row[mid]<1:
                    high-=1
                else:
                    low+=1
            return res+1
        lst = []
        for i in range(len(mat)):
            r = check(mat[i])
            lst.append([r,i])
        lst=sorted(lst)
        print(lst)
        ans = [ ]
        for j in range(k):
            ans.append(lst[j][1])
        return ans