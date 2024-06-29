class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        lst = [ ]
        for num,fre in c.items():
            lst.append([fre,num])
        lst =sorted(lst)[::-1]
        print(lst)
        s= 0
        cnt = 0
        half_len = len(arr) // 2
        for i,j in lst:
            s+=i
            cnt +=1
            if s>=half_len:
                return cnt
        