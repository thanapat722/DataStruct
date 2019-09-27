def aLine(s):
    res = ''
    for i in range(1, len(s)):
        res = s[i] + res
    res = res + s
    res = '.'.join(res)
    res = res
    return res

def gen_pattern(s):
    n = 4*len(s)-3
    mid = aLine(s) + '\n'
    for i in range(1,len(s)):
        r = aLine(s[i:len(s)])
        r = r.center(n,'.')
        r = r + '\n'
        mid = r + mid + r
    return mid

s = 'กขคงจ'

print(gen_pattern(s))
