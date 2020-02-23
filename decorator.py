

def decorator(func):
    def wrapper():
        print('方法增强')
        func()
    return wrapper


def f():
    print('想要实现的方法')

r = decorator(f)
r()

@decorator
def f2():
    print('想要实现的方法2')

f2()