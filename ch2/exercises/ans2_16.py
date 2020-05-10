nums = [1, -200, 3, 400, 5, -8, 9, 15, -100, 2]
nums.sort()  #先将列表升序排序
print(nums)
max_num = max(nums)
max_2nd = nums[-2]
min_num = min(nums)
min_2nd = nums[1]
print(max_num, max_2nd, min_num, min_2nd)
