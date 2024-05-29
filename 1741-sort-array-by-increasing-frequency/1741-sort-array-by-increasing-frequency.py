class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        lst = []
        c = Counter(nums)
        for key,value in c.items():
            lst.append([value,key])
        ans =  []
        pre = 0
        n = len(lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if lst[j][0] > lst[j+1][0]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                elif lst[j][0] == lst[j+1][0] and lst[j][1] < lst[j+1][1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        print(lst)
        ans = [ ]
        for fre,val in lst:
            ans.extend([val]*fre)
        print(ans) 
        return ans

