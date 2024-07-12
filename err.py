def err(a):
    try:
        10 / a
    except Exception as e:
        print("except")
        print(e)
    finally:
        print("finally")


err(0)

f = None
try:
    f = open("io0000.py", 'r')
    for line in f.readlines():
        print(line)
    f.close()
except Exception as e:
    print(e)
finally:
    if f:
        f.close()
