class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i in matches:
            win,los = i[0],i[1]
            if win not in d:
                d[win] = "w"
            if d[los]=="w":
                d[los]=0
            d[los]+=1
        res = [[],[]]
        for i in d:
            if d[i]=="w":
                res[0].append(i)
            if d[i]==1:
                res[1].append(i)
        res[0].sort()
        res[1].sort()
        return res

        