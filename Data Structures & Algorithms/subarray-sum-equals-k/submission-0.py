class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicti={0:1}
        s=0
        count=0
        for i,inte in enumerate (nums):
            s+=inte
            req=s-k
            if req in dicti:
                count+=dicti[req]
            dicti[s]=dicti.get(s, 0)+1
        return count