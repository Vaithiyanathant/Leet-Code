class Solution:
    def minimumPushes(self, word: str) -> int:
        lst = [0]*8
        cnt = 0 
        incr = 1
        print(lst)
        for i in range(1,len(word)+1):
            cnt+=incr 
            if i%8 ==0:
                incr+=1

        return cnt