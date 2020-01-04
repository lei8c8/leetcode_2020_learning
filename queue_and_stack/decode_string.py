class Solution:
    def decodeString(self, s: str) -> str:
        cur_string, stack, cur_value = '', [], 0
        for ch in s:
            if ch == '[':
                stack.append(cur_string)
                stack.append(cur_value)
                cur_string = ''
                cur_value = 0
            elif ch == ']':
                num = stack.pop()
                pre_string = stack.pop()
                cur_string = pre_string + num * cur_string
            elif ch.isdigit():
                cur_value = cur_value * 10 + int(ch)
            else:
                cur_string = cur_string + ch
        return cur_string