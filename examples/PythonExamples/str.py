some_name = "Nafisa Plummer"

# 判断是否为空字符串
print(some_name.isspace())

# 统计字符 a 的数量
print(some_name.count("a"))

# 判断是否是字母
print(some_name.isalpha())

# 判断是否为字母或数字
some_str = "Number is 25"
print(some_str.isalnum())

some_digit = "25"

# 判断是否为数字
print(some_digit.isdigit())

c_digit = "二十五"

# 判断是否为数字
print(c_digit.isnumeric())

# 判断是否为大写字母组成的字符串
upper_str = "HELLO"
print("Uppercase str: ", upper_str.isupper())

# 判断是否为小写字母组成的字符串
lower_str = "hello"
print("Lowercase str: ", lower_str.islower())

some_str = "Hello\nWorld"
print(some_str.splitlines())

some_str = "Willard Cote,Livia Pitts,Nafisa Plummer"
print(some_str.split(","))

# 去空字符串
space_str = f" {some_name} "
print(space_str.strip())
print(space_str.lstrip())
print(space_str.rstrip())

some_title = "hello world"

# 转换为标题格式的字符串
some_title = some_title.title()
print(some_title)

# 判断是否为标题大小写的字符串
print(some_title.istitle())

# 拼接列表中的元素为字符串
some_list = ["Willard Cote", "Livia Pitts", "Nafisa Plummer"]

join_str = ", ".join(some_list)
print(join_str)

print(join_str.replace(",", "、"))

print(some_name.startswith("N"))
print(some_name.endswith("r"))

# 移除指定前缀字符串
print(some_name.removeprefix("N"))
# 移除指定后缀字符串
print(some_name.removesuffix("r"))


x = "abcdefghijklmnopqrstuvwxyz"
y = "1234567890abcdefghijklmnop"

# 生成转换表
translate_table = str.maketrans(x, y)
# 使用指定的转换表替换字符串中的每一个字符
print("hello world".translate(translate_table))