import json
import os
import time

import tornado.web
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient

import config


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('sunck is a good man')


class SunckHandler(RequestHandler):
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        print(self.word1, self.word2)
        self.write('sunck is a nice man', )


class GetHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a')
        b = self.get_query_argument('b')
        c = self.get_query_argument('c', strip=False)
        print(a, b, "*" + c + "*")
        self.write('zhangmanyu is a good women')


class GetHugeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        alist = self.get_query_argument('a', strip=True)
        print(alist[0], alist[1])
        self.write('HuGe is very cool')


class UpFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')

    def post(self, *args, **kwargs):
        print(self.request.files)
        FileDict = self.request.files
        for Inputname in FileDict:
            print(Inputname)
            File_Arr = FileDict[Inputname]
            print(File_Arr)
            for File_Obj in File_Arr:
                print(File_Obj)
                File_Path = os.path.join(config.BASE_DIRS, 'upfile/'+ File_Obj.filename)
                with open(File_Path, 'wb') as f:
                    f.write(File_Obj.body)
        self.write("OK。。。。。")


class Parameter_Path(RequestHandler):
    def initialize(self, word3, word4):
        self.world3 = word3
        self.world4 = word4

    def get(self, *args, **kwargs):
        self.write("OK")


class LiuyifeiHandler(RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):
        print(h1 + '-' + h2 + '-'+ h3)
        self.write('sun is very Good.....')


class RequestsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.uri)
        print(self.request.files)
        print(self.request.method)
        # print(self.request.data)
        # print(self.request.json)
        print(self.request.cookies)
        print('************************')
        print(self.request.headers)
        # print(self.request.auth)
        print(self.request.path)
        print(self.request.version)
        print(self.request.remote_ip)
        print(self.request.query)
        print(self.request.body)
        self.write("啦啦啦啦，德玛西亚")



class PostParameter(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html')
    def post(self, *args, **kwargs):
        name =self.get_body_argument('username')
        print(name)
        passwd = self.get_query_argument('passwd')
        print(passwd)
        hobbyList = self.get_body_arguments("hobby")
        print(hobbyList)
        self.write('sun is a handsome ')


# class HomeHandler(RequestHandler):
#     def get(self, *args, **kwargs):
#         num1 = 100
#         self.render('home.html', num = num1)


class EscapeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1>只有我才能带领你们走向胜利</h1>"
        self.render('home.html', str=str)


class PcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('sunck', 'cool')
        self.write('OK...........')


class SCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie('sun','cool')
        self.write('OK...................')


class GCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.get_secure_cookie('sun')


class CookieCountHandler(RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie('cookie', None)
        if count == None:
            count = 1
            # now_time = time()

        else:
            count_num = int(count)
            count_num += 1
            self.render('cookienum.html', count_num = count_num)

class MainHandler(RequestHandler):
    def get(self):
        self.finish("haha")
        self.write("Hello, world")


class TesHandler(RequestHandler):
    def get(self):
        self.write('hello, world!')
        self.finish("hehe")


class StudentHandler(RequestHandler):
    def on_Response(self, response):
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
            self.write(data)
        self.finish()
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        client = AsyncHTTPClient()
        client.fetch(url, self.on_Response)

        # time.sleep(30)
        self.write('数据接收完成。')


class StudentsMainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('main.html')


class StudentsAsyHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        client = AsyncHTTPClient()
        result = yield client.fetch(url)
        if result.error:
            self.send_error(500)
        else:
            data = json.loads(result.body)
            self.write(data)


class MainAsyHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('main.html')


class StudentsIoHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        result = yield self.GetData()
        self.write(result)

    @tornado.gen.coroutine
    def GetData(self):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        client = AsyncHTTPClient()
        result = yield client.fetch(url)
        if result.error:
            res = {'res': 0}
        else:
            res = result.body
        raise tornado.gen.Return(res)


class MainIoHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('main.html')