from typing import List


class Solution:

    def longest_common_prefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        prefix = ""

        strs.sort()

        for i in strs[0]:
            if strs[-1].startswith(prefix+i):
                prefix += i
            else:
                break

        return prefix





s = Solution()
print(s.longest_common_prefix(["flower","flow","flight"]))

