# leetcode move-zeros
# Time complexity: 0(n)
# Space complexity: 0(1)

def move_zeroes(nums):
    position=0

    # Move all the non-zero numbers to the front
    for num in nums:
        if num != 0:
            nums[position] = num
            position += 1

    # Feel the remaining positions with zeros
    while position < len(nums):
        nums[position] = 0
        position += 1


nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)  

nums2 = [7, 0, 6, 8, 0, 4]
move_zeroes(nums2)
print(nums2)
