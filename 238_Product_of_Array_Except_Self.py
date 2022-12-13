class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        H, L = [[1,1]], len(nums)
        for i in range(L-1):
            H.append([H[i][0]*nums[i], H[i][1]*nums[-i-1]])
        print(H)
        return [H[i][0] * H[-i-1][1] for i in range(L)]
