"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""

def solution(str):
    s_arr = list(str)
    for i, s in enumerate(s_arr):
        if s == ' ':
            s_arr[i] = '%20'
    return ''.join(s_arr)

def solution2(s):
    # 终极解法    
    # return s.replace(' ', '%20')
    # append
    a = []

    for c in s:
        if c == ' ':
            a.append('%20')
        else:
            a.append(c)
            
    return ''.join(a)
    



def test_solution():
    assert solution('We are happy.') == 'We%20are%20happy.'
    assert solution2('We are happy.') == 'We%20are%20happy.'

