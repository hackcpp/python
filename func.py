def add(x, y):
    return x + y  # 通过return 返回结果


print(add(1, 2))


def echo(n="liuheng"):
    print(n)


echo()
echo("lucas")


def calc(*nums):
    print(type(nums))
    s = 0
    for num in nums:
        s = s + num
    return s


print(calc(1, 2, 3))


def person(**kw):
    print(type(kw))
    for k, v in kw.items():
        print(k + ":" + str(v))


person(name="liuheng", age=18)


def person2(*, city, job):
    print(city + ":" + job)


# 调用是字典参数的key 只能是city,job
person2(city="jx", job="rd")
# TypeError: person2() got an unexpected keyword argument 'job2'
# person2(city="jx", job2="rd")
