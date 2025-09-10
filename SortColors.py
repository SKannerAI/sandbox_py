from typing import List


class Solution:
    def sortColors(self, nums: List[int]):
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        R, W, B = counts

        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B

    # instantiate the class
sol = Solution()

# input list
colors = [2, 0, 2, 1, 1, 0]

# invoke the method
sol.sortColors(colors)

print(colors)  # Output: [0, 0, 1, 1, 2, 2]
