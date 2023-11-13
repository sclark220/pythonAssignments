class Solution:
    
    #Function to sort an array of 0s, 1s, and 2s.
    def sort012(self,arr,n):
        low=0
        high=n-1
        mid=0
        
        #iterating until mid pointer is less than or equal to high.
        while mid<=high:
            
            #if element at mid is 0, swap with element at low and move both pointers.
            if arr[mid]==0:
                arr[mid] , arr[low] = arr[low] , arr[mid]
                mid+=1
                low+=1
                
            #if element at mid is 1, move mid pointer.
            elif arr[mid]==1:
                mid+=1
                
            #if element at mid is 2, swap with element at high and move high pointer.
            else:
                arr[mid] , arr[high] = arr[high] , arr[mid]
                high-=1

class AWayBetterSolution:
    def sort012(array):
        return sorted(array)