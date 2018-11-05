import time
import threading



def longIO():
    print('开始耗时操作')
    time.sleep(10)
    print('结束耗时操作')
    yield "sunck is a good man"


def gencoroutine(func):
    def wrappe(*args, **kwargs):
        print('?????????????????????????????')
        gen1 = func()
        gen2 = next(gen1)

        def run(g):
            result = next(g)
            try:
                gen1.send(result)
            except StopIteration as e:
                pass
        threading.Thread(target=run, args=(gen2,)).start()
    return wrappe

@gencoroutine
def RequestA():
    print('请求开始A')
    res = yield longIO()
    print('接受到run函数返回的数据 %s' % res)
    print('结束请求A')


def RequestB():
    print('请求开始B')
    time.sleep(3)
    print('请求结束B')


def main():
    RequestA()
    RequestB()


if __name__ == '__main__':
    main()


# import time
# import threading

# def genCoroutine(func):
#     def wrapper(*args, **kwargs):
#         gen1 = func()#reqA的生成器
#         gen2 = next(gen1)#longIo的生成器
#         def run(g):
#             res = next(g)
#             try:
#                 gen1.send(res)#返回给reqA数据
#             except StopIteration as e:
#                 pass
#         threading.Thread(target=run,args=(gen2,)).start()
#     return wrapper
#
# #handler获取数据(数据库、其他服务器、循环耗时)
# def longIo():
#     print("开始耗时操作")
#     time.sleep(5)
#     print("结束耗时操作")
#     #返回数据
#     yield "sunck is a good man"
#
# #一个客户单的请求
# @genCoroutine
# def reqA():
#     print("开始处理reqA")
#     res = yield longIo()
#     print("接收到longIo的响应数据：", res)
#     print("结束处理reqA")
#
# #另一个客户端的请求
# def reqB():
#     print("开始处理reqB")
#     time.sleep(2)
#     print("结束处理reqB")
#
# #tornado服务
# def main():
#     reqA()
#     reqB()
#     while 1:
#         time.sleep(0.1)
#         pass
#
# if __name__ == "__main__":
#     main()









