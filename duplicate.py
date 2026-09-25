#-----------------------------------------------------------------------------
#PRINT ELEMENT WITHOUT DUPLIACATION FROM LIST
#-----------------------------------------------------------------------------
nums = [1,4,5,67,78,9,23,5,6,7,8,7,8,12,2,3,2,3,4,11,11,0,0,4]

for i in range(len(nums)):
    isDuplicate = True

    for j in range(i):
        if nums[i] == nums[j]:
            isDuplicate = False
            break
    if  not isDuplicate:
        print(nums[i], end=" ,")

        

       
