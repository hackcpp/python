# 元组 tuple 不可修改
print("-------------------tuple---------------------")
names = ("liuheng", "lucas", "clr")
print(names)
names[1]
# TypeError: 'tuple' object does not support item assignment
# names[1] = "222"
names = names[1:]
print(names)

print("------------------list----------------------")
# 列表 list
names = ["liuheng", "lucas"]
print(names)
# 追加
names.append("clr")
print(names)
# 插入
names.insert(0, "chenglirong")
print(names)
# 删除
names.pop(1)
print(names)
# 访问
print(names[0])
# 遍历
for name in names:
    print(name)

# 列表生成式
[x for x in range(10) if x % 2 == 0]
new_names = ["_" + name for name in names]
print(new_names)
# 切片
print(new_names[1:])

print("------------------set----------------------")
# 集合 set 去重，集合中的元素唯一
names = set(["liuheng", "liuheng", "lucas"])
print(names)
# 集合生成式
names = {x + "xxx" for x in names}
print(names)

print("------------------dict----------------------")
# 字典 dict
persons = {"liuheng": 18, "lucas": 12}
print(persons)
print(type(persons))
# 增
persons["crl"] = 18
print(persons)
# 改
persons["liuheng"] = 9
print(persons)
# 删
persons.pop("lucas")
print(persons)

# 遍历
for k in persons.keys():
    print(k)

for v in persons.values():
    print(v)

for k, v in persons.items():
    print(k + ":" + str(v))

# 字典生成式
d = {i: i * i for i in range(6)}
print(d)
