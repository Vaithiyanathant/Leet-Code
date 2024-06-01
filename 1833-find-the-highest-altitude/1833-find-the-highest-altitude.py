class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = [0]
        for i in range(len(gain)):
            pre.append(pre[-1]+gain[i])
        print(pre)
        return max(pre)
