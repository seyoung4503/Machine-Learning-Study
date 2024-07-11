
nums = [1, 1, 1, 2, 2, 3]
l=1

# for r in range(1,len(nums)):
#     # print(nums[r], nums[r-1])
#     print(r)
#     if nums[r]!=nums[r-1]:
#         print(l, nums[l])
#         nums[l]=nums[r]
#         l+=1

# print(nums)
# print(l)


k = 1
ctr = 0
for i in range(1, len(nums)):
    print("nums[", i, "], nums[", i-1, "] : ", nums[i], nums[i-1])
    if nums[i] != nums[i-1]:
        nums[k] = nums[i]
        k += 1
        ctr = 0
    elif ctr < 1 and nums[i] == nums[i-1]:
        nums[k] = nums[i]
        k += 1
        ctr += 1
    print("ctr : ", ctr)
    print(i)
        
print(k)
print(nums)

#  169. Majority Element

sdq
                    
# avg = sum(nums)/len(nums)
# print(avg)
# min_val = 10**9+1
# element = 0
# for i in nums:
#     a = abs(avg - i)
#     if min_val > a:
#         min_val = a
#         element = i

# return element

'''
해시맵 아이디어 
해시맵을 사용하면 for idx, value in enumerate(numbers) 은 O(n)
if value not in index_dict 은 O(1)

최종적으로 리스트에 비해 O(n^2)에서 O(n)으로 줄임
'''

        # indexed_dict = {value: idx for idx, value in enumerate(numbers)}
        
#         index_dict = {}
        
#         for idx, value in enumerate(numbers):
#             if value not in index_dict:
#                 index_dict[value] = []
#             index_dict[value].append(idx)
        
#         print(index_dict)
                
            
                
                
                