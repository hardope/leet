class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        next = []
        for i in nums:
            if i not in new:
                new.append(i)
            else:
                next.append(i)

        for i in set(next):
            new.remove(i)

        return new[0]
