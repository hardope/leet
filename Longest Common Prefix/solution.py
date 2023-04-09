class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        example = strs[0]
        count = 0
        out = ""
        if len(strs) == 1 or strs[0] == "":
            return strs[0]

        for i in example:
            for j in range(len(strs)):
                try:
                    assert i == strs[j][count]
                except:
                    return out
            out+=i
            count+=1
        return out 
