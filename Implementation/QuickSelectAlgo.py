import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums=nums
        self.k=k
        return self.quickselect(0,len(nums)-1)
        
        
    def partition(self,start,end):
        pivot_ind=random.randint(start,end) # random select pivot
        pivot=self.nums[pivot_ind]
        self.nums[pivot_ind],self.nums[end]=self.nums[end],self.nums[pivot_ind]
        
        pivot_index=start
        
        for i in range(start,end+1):
            if self.nums[i]>pivot:
                self.nums[i],self.nums[pivot_index]=self.nums[pivot_index],self.nums[i]
                pivot_index+=1
                
        self.nums[end],self.nums[pivot_index]=self.nums[pivot_index],self.nums[end]
        return pivot_index
        
        
    def quickselect(self,start,end):
        k=self.k -1
        if start<=end:
            
            pivot_index=self.partition(start,end)
            if pivot_index>k:
                return self.quickselect(start,pivot_index-1)
            elif pivot_index<k:
                return self.quickselect(pivot_index+1,end)
            else:
                return self.nums[k]