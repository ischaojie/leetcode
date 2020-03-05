
# 装饰器实现


def singleton(func):
    instances = {}

    def wrapper(*args, **kw):
        if func not in instances:
            instances[func] = func(*args, **kw)
        return instances[func]
    return wrapper


# 利用__new__实现
class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
