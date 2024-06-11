class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ina = {}
        outa = {}
        for i in range(len(arr1)):
            if arr1[i] in ina:
                ina[arr1[i]]+=1
            elif arr1[i] not in ina:
                ina[arr1[i]]=1
            if arr1[i] not in arr2:
                if arr1[i] in outa:
                    outa[arr1[i]]+=1
                else:
                    outa[arr1[i]]=1
        print(ina)
        print(outa)
        ans = [ ]
        for i in range(len(arr2)):
            for k in range(ina[arr2[i]]):
                ans.append(arr2[i])
        souta = sorted(outa)
        for h in souta:
            for l in range(outa[h]):
                ans.append(h)
        return ans

        