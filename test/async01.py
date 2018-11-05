import time
import threading


def longIO(callback):
    def run(cb):
        print('开始耗时操作')
        time.sleep(10)
        print('结束耗时操作')
        cb('只有我才能带领你们走向胜利。。。。。。。。。。。')
    threading.Thread(target=run, name='runlongIO', args=(callback, )).start()


def finish(data):
    print('开始处理回调函数')
    print('接受到run函数返回的数据 %s' % data)
    print('结束处理回调函数')


def RequestA():
    print('请求开始A')
    longIO(finish)
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
