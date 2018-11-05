import time

import uuid
import base64
import threading

# 生成一串UUID表示唯一标识
# my_uuid = uuid.uuid4().bytes + uuid.uuid4().bytes
# print(my_uuid)


# yield机制理解
# def func1():  # 生成器函数
#     print("ok1")
#     x = 10  # 函数内局部变量x赋值为10
#     print(x)
#     x = yield 1  # 这里就是send函数的关键
#     # 之前我们创建的生成器，yield左边都是没有值（我现在不是很确定这里是不是应该叫做返回值，那就先用值代替）。
#     # 现在我们的x会接收到一个值，这个值是什么，从哪里来的？我们继续看下去
#     print(x)
#     yield x  # 这里试第二个断点
#
#
# f1 = func1()  # 获取生成器对象
# data = next(f1)

# 函数内部定义函数的理解
def run():
    def wrapper():
        print('Hello')

    def wrappers():
        print('sun')

    wrapper()    # 想普通函数一样调用一下就可以返回
    wrappers()


run()


# tornado异步， 简单实现
def genCoroutine(func):
    def wrapper(*args, **kwargs):
        gen1 = func()   # reqA的生成器
        gen2 = next(gen1)   # longIo的生成器

        def run(g):
            res = next(g)
            try:
                gen1.send(res)  # 返回给reqA数据
            except StopIteration as e:
                pass
        threading.Thread(target=run,args=(gen2,)).start()
    return wrapper


# handler获取数据(数据库、其他服务器、循环耗时)
def longIo():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    #返回数据
    yield "sunck is a good man"


# 一个客户单的请求
@genCoroutine
def requestA():
    print("开始处理reqA")
    res = yield longIo()
    print("接收到longIo的响应数据：", res)
    print("结束处理reqA")


# 另一个客户端的请求
def requsetB():
    print("开始处理reqB")
    time.sleep(2)
    print("结束处理reqB")


# tornado服务
def main():
    requsetA()
    requsetB()
    while 1:
        time.sleep(0.1)
        pass


if __name__ == "__main__":
    main()
