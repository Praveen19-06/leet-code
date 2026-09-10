class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
     
        stack=[]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    for k in range(j+1,len(nums2)):        
                        
                        
                            if nums2[k]>nums2[j]:
                                stack.append(nums2[k])
                                break
                    else:
                        stack.append(-1)
                            
        return stack                
              

        