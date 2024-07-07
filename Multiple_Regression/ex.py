
#         i, j = 0, 0
        
        
#         nums = []
#         if n * m > 0:
#             for _ in range(n+m):

#                 if i < m+n:
#                     a = nums1[i]
#                 if j < n:
                    
#                     b = nums2[j]
#                 elif j >= n:
#                     b = 0
#                 elif i >= n+m:
#                     a = 0
#                 # print(a, b)
#                 if a <= b:
#                     nums.append(a)
#                     i += 1
#                 elif a > b > 0:
#                     nums.append(b)
#                     j += 1
#                     # print(j)
#                     print(a)

#                 if i >= m:
#                     nums.append(b)
#                     j += 1
#                 if j >= n:
#                     nums.append(a)
#                     i += 1

#             # for x in range(n+m):
#             #     # nums[x]
#             #     nums1[x] = nums[x]
#             print(nums)
#         elif n > 0:
#             for i in range(n):
#                 nums1[i] = nums2[i]
            
        
        
        
        
        
        
# #         i, j = 0, 0
# #         if m*n > 0:
# #             a, b = nums1[0], nums2[0]
# #             for _ in range(m + n):
# #                 print(a, b)
# #                 # print(i, j)

# #                 if a == 0:
# #                     # b = nums2[j]
# #                     print(j)
# #                     j+= 1
# #                     nums1[_] = b
# #                     continue
# #                 if b == 0:
# #                     # a = nums1[i]
# #                     # print(j)
# #                     i += 1
# #                     nums1[_] = a
# #                     continue
                    
                    
                
# #                 if a <= b:
# #                     nums1[_] = a
# #                     i += 1
# #                     a = 0
# #                     if i < m:
# #                         a = nums1[i]

# #                 else:
# #                     nums1[_] = b
# #                     j += 1
# #                     b = 0
# #                     if j < n:
# #                         b = nums2[j]
                

# #         elif n > 0:

# #             print("xxxx")
# #             nums1[0] = nums2[0]

# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# n = 3
# m = 3

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
i, j = 0, 0
a, b = nums1[i], nums2[j]
for _ in range(n+m):
    # a, b = nums1[i], nums2[j]
    print(a, b)
    # print(i, j)
    
    
    if a <= b:
        nums1[_] = a
        i += 1
        # a = nums1[i]
        # a = 10**9
        if i > m:
            a = 10**9
        else:
            a = nums1[i]

    elif b < a:
        nums1[_] = b
        j += 1
        # b = nums2[j]
        # b = 10**9
    
    
    
        if j > n-1:
            b = 10 **9
        else:
            print("j ", j)
            b = nums2[j]
print(nums1)