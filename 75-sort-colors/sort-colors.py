class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0

        for num in nums:
            match num:
                case 0:
                    red += 1
                case 1:
                    white += 1
                case 2:
                    blue += 1
        
        for i in range(red):
            nums[i] = 0

        for i in range(red, red + white, 1):
            nums[i] = 1
        for i in range(red + white, red + white + blue, 1):
            nums[i] = 2

        return

        