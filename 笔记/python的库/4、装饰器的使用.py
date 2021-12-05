"""
python @符号是装饰器的语法糖
https://www.cnblogs.com/ellisonzhang/p/11196390.html
"""
"""一、入门用法：日志打印器"""
# def logger(func):
#     def wrapper(*args, **kw):
#         print('我准备开始计算：{} 函数了:'.format(func.__name__))
#         # 真正执行的是这行。
#         func(*args, **kw)
#         print('啊哈，我计算完啦。给自己加个鸡腿！！')
#     return wrapper
#
# @logger
# def add(x, y):
#     print('{} + {} = {}'.format(x, y, x+y))
#
# add(10, 15)
"""二、入门用法：时间计时器"""
# import time
# def print_time(func):
#     def l_time(*args, **kwargs):
#         print("====")
#         l_time_1 = time.time()
#         func(*args, **kwargs)
#         l_time_2 = time.time()
#         count_time = l_time_2 - l_time_1
#         print("程序运行总计耗时为{}秒".format(count_time))
#     return l_time
# @print_time
# def run():
#     print("开始运行")
#     time.sleep(10)
#
# run()
"""三、进阶用法：带参数的函数装饰器"""
# def say_hello(contry):
#     def wrapper(func):
#         def deco(*args, **kwargs):
#             if contry == "china":
#                 print("你好!")
#             elif contry == "america":
#                 print('hello.')
#             else:
#                 return
#
#             # 真正执行函数的地方
#             func(*args, **kwargs)
#         return deco
#     return wrapper
#
#
# @say_hello("china")
# def american():
#     print("我来自中国。")
#
# @say_hello("america")
# def chinese():
#     print("I am from America.")
#
#
# american()
# chinese()
"""四、高阶用法：不带参数的类装饰器"""
# 基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
# __init__ ：接收被装饰函数
# __call__ ：实现装饰逻辑。

class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]: the function {func}() is running...".format(func=self.func.__name__))
        return self.func(*args, **kwargs)

@logger
def say(something):
    print("say {}!".format(something))

say("hello")

"""五、高阶用法：带参数的类装饰器"""
# 带参数和不带参数的类装饰器有很大的不同。
#
# __init__ ：不再接收被装饰函数，而是接收传入参数。
# __call__ ：接收被装饰函数，实现装饰逻辑。

class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func): # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running..."\
                .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper  #返回函数

@logger(level='WARNING')
def say(something):
    print("say {}!".format(something))

say("hello")

"""六、使用偏函数与类实现装饰器"""
# 绝大多数装饰器都是基于函数和闭包实现的，但这并非制造装饰器的唯一方式。
# 事实上，Python 对某个对象是否能通过装饰器（ @decorator）形式使用只有一个要求：decorator 必须是一个“可被调用（callable）的对象。
# 对于这个 callable 对象，我们最熟悉的就是函数了。
# 除函数之外，类也可以是 callable 对象，只要实现了__call__ 函数（上面几个盒子已经接触过了），还有比较少人使用的偏函数也是 callable 对象。
# 接下来就来说说，如何使用 类和偏函数结合实现一个与众不同的装饰器。
# 如下所示，DelayFunc 是一个实现了 __call__ 的类，delay 返回一个偏函数，在这里 delay 就可以做为一个装饰器。（以下代码摘自 Python工匠：使用装饰器的小技巧）
# import time
# import functools
#
# class DelayFunc:
#     def __init__(self,  duration, func):
#         self.duration = duration
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f'Wait for {self.duration} seconds...')
#         time.sleep(self.duration)
#         return self.func(*args, **kwargs)
#
#     def eager_call(self, *args, **kwargs):
#         print('Call without delay')
#         return self.func(*args, **kwargs)
#
# def delay(duration):
#     """
#     装饰器：推迟某个函数的执行。
#     同时提供 .eager_call 方法立即执行
#     """
#     # 此处为了避免定义额外函数，
#     # 直接使用 functools.partial 帮助构造 DelayFunc 实例
#     return functools.partial(DelayFunc, duration)
# # functools库如下用法
# # cmp_to_key	将一个比较函数转换关键字函数
# # partial	针对函数起作用，并且是部分的
# # reduce	与python内置的reduce函数功能一样
# # total_ordering	在类装饰器中按照缺失顺序填充方法
# # update_wrapper	更新一个包裹函数，使其看起来更像被包裹的函数
# # wraps	可用作一个装饰器，简化调用update_wrapper过

# @delay(duration=2)
# def add(a, b):
#     return a+b
#
# a = add(10, 15)
# print(a)