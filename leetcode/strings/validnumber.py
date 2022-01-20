'''
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
'''
class Solution:
    def isNumber_State(self, s: str) -> bool:
        state = [{}, {'blank':1, 'sign':2, 'digit':3, ".":4}{'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
        cur_state = 1
        for c in s:
            if c >= '0' and c<='9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+','-']:
                c = 'sign'
            if c not in state[cur_state].keys():
                return False
            cur_state = state[cur_state][c]
        if cur_state not in [3,5,8,9]:
            return False
        return True
    
    def isNumber_regex(self, s):
        import re 
		#Example:               +-     1 or 1. or 1.2 or .2   e +- 1     
        engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))(e[+-]?\d+)?$")
        return engine.match(s.strip(" "))
    
    def isNumber(self,s):
        if not s:
            return False
        s = s.strip()
        sign = True
        econstant = True
        decimal = False
        numseen = False
        eseen = False
        for i in range(len(s)):
            if ord(s[i])-ord('0') >= 0 and ord(s[i])-ord('0') <= 9:
                numseen = True
                econstant = True
            elif s[i] == '.':
                if eseen or decimal:
                    return False
                decimal = True
            elif s[i] == 'e':
                if eseen or not numseen:
                    return False
                eseen= True
                econstant = False
            elif s[i] == "+" or s[i] == '-':
                if i!=0 and s[i-1] != 'e':
                    return False
            else:
                return False
        return numseen and econstant
            
sol = Solution()
s = "e3"
print(sol.isNumber(s))