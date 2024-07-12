# f = open("io.py", 'r')
# for line in f.readlines():
#     print(line)
# f.close()

f = None
try:
    f = open("io.py", 'r')
    for line in f.readlines():
        print(line)
    f.close()
except Exception as e:
    print(e)
finally:
    if f:
        f.close()

with open("io.py", 'r') as f:
    for line in f.readlines():
        print(line)
