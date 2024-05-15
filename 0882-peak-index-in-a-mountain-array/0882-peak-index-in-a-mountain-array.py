class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0 
        high = len(arr)-1
        while(low<=high):
            mid = (low + high )//2
            print(mid)
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid+1]:
                high = mid-1
            else:
                low = mid +1
        return 0
                
        