
import re

#正则表达式：字符串模式 （判断字符串是否符合一定的标准）

#创建模式对象

pat = re.compile("AA")              #此处AA，是正则表达式，用来验证其他字符串
# m = pat.search("AAAAAABBBBB")       #search字符串被校检的内容
# m = pat.search("ABBBBB")            #search方法，继续宁比对查找

# m = re.search("asd","Aasd")           #前面的字符串是规则，后面的字符串是被校验的对象
# print(m)

# print(re.findall("a","AsdaDFGa"))       #前面字符串时正则表达式，后面字符串是被校验的字符串

# print(re.findall("[A-Z]","AsdaDFGa"))

# print(re.findall("[A-Z]+","AsdaDFGa"))

#sub 替换

# print(re.sub("a","A","abcdcasd"))           #找到a，用A替换

# 建议在正则表达式中，被比较的字符串前加上r，不用担心转义字符的问题
# a= r"\aabb-\'"
# print(a)