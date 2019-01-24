'''
题目：有效数字
描述：
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
'''


'''
字符串从e出分开，左边是小数，右边是整数, 76 ms
'''
class Solution:
    def isInt(self, s):
        if s == '': return False
        if s[0] in ['+', '-']:
            s = s[1:]
        if s == '': return False
        for c in s:
            if c > '9' or c < '0':
                return False
        return True

    def isFloat(self, s):
        if s == '': return False
        if s[0] in ['+', '-']:
            s = s[1:]
        if s == '': return False
        if s == '.':
            return False
        if s.count('.') > 1:
            return False
        for c in s:
            if c == '.' or '0' <= c <= '9':
                continue
            else:
                return False
        return True

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0: return False
        data = s.split('e')
        if len(data) > 2:
            return False
        elif len(data) == 2:
            return self.isFloat(data[0]) and self.isInt(data[1])
        else:
            return self.isFloat(data[0])
