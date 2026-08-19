class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


# Main program
if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    solution = Solution()
    result = solution.containsDuplicate(nums)

    print("Input:", nums)
    print("Output:", result)