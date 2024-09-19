class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        ans = []
        i = 0
        j = len(nums) - 1

        while i < j:
            ans.append((nums[j] + nums[i]) / 2)
            i += 1
            j -= 1
        return min(ans)
