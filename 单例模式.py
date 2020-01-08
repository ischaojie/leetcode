

def singleton(func):
    instances = {}
    def getinstance(*args, **kw):
        if func not in instances:
            instances[func] = func(*args, **kw)
        return instances[func]
    return getinstance

