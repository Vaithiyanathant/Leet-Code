class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs = sorted(heights)
        h = heights
        if h ==hs:
            return 0
        else:
            cnt = 0
            for i in range(len(h)):
                if h[i]!=hs[i]:
                    cnt+=1
            return cnt

