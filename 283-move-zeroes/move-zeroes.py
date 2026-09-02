class Solution:
    def moveZeroes(self, nums):
     
        count =0
        new=[]
        for i in range(len(nums)):
            if nums[i]==0:
                
                count+=1
            else:
                new.append(nums[i])    
                
        for j in range(count):
            new.append(0)
        nums[:]=new
        return new 
  
        
        