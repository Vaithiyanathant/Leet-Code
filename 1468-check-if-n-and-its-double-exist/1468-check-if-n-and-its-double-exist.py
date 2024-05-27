class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def helper(arr,num):
            low = 0
            high = len(arr)-1
            while(low<=high):
                mid = (low + high)//2
                if num == arr[mid]:
                    print(num)
                    return True
                elif arr[mid] <num:
                    low= mid + 1
                else:
                    high = mid-1
            return False
        arr = sorted(arr)
        for i in  range(len(arr)):
            if arr.count(0)>=2:
                return True
            elif helper(arr,(arr[i]*2)) and arr[i]!=0:
                return True
        return False
        