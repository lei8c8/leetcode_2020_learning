from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_items, ans = defaultdict(list), []
        for s in strs:
            key = tuple(sorted(s))
            group_items[key].append(s)
        for key in group_items:
            ans.append(group_items[key])
        return ans