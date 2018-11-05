import time
import threading

gen = None

def longIO():
    def run():
        try:
            print('开始耗时操作')
            time.sleep(10)
            global gen
            gen.send('我在哪过来的')
        except StopIteration:
            print('结束耗时操作')

    threading.Thread(target=run, name='runlongIO').start()


# def finish(data):
#     print('开始处理回调函数')
#     print('接受到run函数返回的数据 %s' % data)
#     print('结束处理回调函数')


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
    global gen
    gen = RequestA()
    print(gen)
    next(gen)
    RequestB()


if __name__ == '__main__':
    main()
