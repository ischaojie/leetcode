import time
def exec_time(func):
    def decorator(*args, **kw):
        start = time.time()
        res = func(*args, **kw)
        print("cost time: {}".format(time.time()-start))
        return res
    return decorator


@exec_time
def func1():
    sum = 0
    for i in range(10*100):
        sum += i
    return sum

print(func1())
