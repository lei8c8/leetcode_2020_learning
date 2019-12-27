from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouped_string, res = defaultdict(list), []
        for string in strings:
            key = [ord(s) - ord(string[0]) for s in string]
            key = tuple([number + 26 if number < 0 else number for number in key])
            grouped_string[key].append(string)
        for key in grouped_string:
            res.append(grouped_string[key])
        return res 