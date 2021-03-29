"""
豆瓣 2021 春 社招
"""

# 1. 书籍作者有 '[美]老刘, 余则成【中】【美】' 等，需要去除作者国籍，
# 假设字符只会有 '()' '[]' '【】' '{}' 四种。国籍信息可能出现在任何位置。
def author_clear(author: str) -> str:
    left_bracket = ["(", "[", "【", "{"]
    right_bracket = [")", "]", "】", "}"]
    temp = author
    res = []

    for i, a in enumerate(temp):
        if a in left_bracket:
            for j, b in enumerate(temp[i+1:]):
                if b in right_bracket:
                    res.extend(temp[:i])
                    temp = temp[j+1:]
    
    return ''.join(res) 



# 2. sql

# 3. 字符串匹配