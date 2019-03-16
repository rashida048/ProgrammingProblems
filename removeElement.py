#Given an array nums and a value val, remove all instances
#of that value in-place and return the new length.
#Do not allocate extra space for another array, you must do this by
#modifying the input array in-place with O(1) extra memory.
#The order of elements can be changed. It doesn't matter what you leave beyond
#the new length.

def remove(nums, val):
    if len(nums) < 1:
        return len(nums)
    if len(nums) ==1 and nums[0]!=val:
        return len(nums)
    elif len(nums) ==1 and nums[0]== val:
        return 0
    i = 0
    j = 0
    for j in nums:
        if j != val:
            nums[i]=j
            i+=1
    return i
        
            

#print(remove([3,2,2,3], 3))
print(remove([0,1,2,2,3,0,2], 2))
