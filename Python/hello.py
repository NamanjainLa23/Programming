# nums = [5,6,7,8]
# target = 12
# numMap = {}


# for i in range(0, len(nums)):
#     comp = target - nums[i]
#     if comp in nums and comp!=nums[i]:
#         print(i, nums.index(comp))
#         b

# print(numMap)


nums = [10,12,10,10,12]
# out_list = []

# for i in range(0,(len(nums)-1)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             out_list.append((i,j))

# print(out_list)

# nums_dict = {}
# count = 0
# for i in range(0, len(nums)):
#     nums_dict[nums[i]] = nums.count(nums[i])

# print(nums_dict)

# for key, value in nums_dict.items():
#     if value > 1:
#         count = count + (value * (value - 1) // 2)  # nc2 - combination 

# print(count)

nums_freq = [0] * max(nums) #create a freequency array to store occurence of number in the original array
# if theere are negative number then add an offset to make it positive to whole array


