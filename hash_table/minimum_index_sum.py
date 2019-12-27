class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1, set2, ans = set(list1), set(list2), []
        lookup1, lookup2, res, both = {}, {}, [], set1 & set2
        for i, v in enumerate(list1):
            lookup1[v] = i
        for i, v in enumerate(list2):
            lookup2[v] = i 
        for r in both:
            res.append((r, lookup1[r] + lookup2[r]))
        res.sort(key = lambda x: x[1])
        min_val = res[0][1]
        for r in res:
            if r[1] == min_val:
                ans.append(r[0])
            else:
                break 
        return ans