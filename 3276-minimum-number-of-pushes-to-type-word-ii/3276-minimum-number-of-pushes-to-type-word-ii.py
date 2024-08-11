class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        lst = [ ]
        for i in c.items():
            lst.append([i[1],i[0]])
        lst = sorted(lst)[::-1]
        incr = 1
        cnt = 0
        ss = []
        for k in lst:
            if k[1] not in ss:
                ss.append(k[1])
            
        d = defaultdict(int)
        print(ss)
        for i in ss:
            d[i]+=incr
            cnt+=1
            if cnt%8==0:
                incr+=1
        res = 0
        for i in ss:
            res+=d[i]*c[i]
        
        return res




        