from views import index
import tornado.web
import config
from orm.sunckMysql import SunckMySQL


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

            # 路由方式
            (r'/', index.IndexHandler),

            # initialize参数传递
            (r'/sunck', index.SunckHandler, {'word1': 'good', 'word2': 'nice'}),

            # get  post参数获取
            (r'/methodget', index.GetHandler),

            # 既能获取get也能获取Post参数
            (r'/huge', index.GetHugeHandler),

            # 模板返回
            (r'/post', index.PostParameter),
            tornado.web.url(r'/parameter', index.Parameter_Path, {'word3': 'hello', 'word4': 'hello01'}),

            # 参数部分
            (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.LiuyifeiHandler),

            #     reqquest对象
            (r'/request', index.RequestsHandler),

            # 文件上传
            (r'/upfile', index.UpFileHandler),

            # 数据返回
            (r'/escape', index.EscapeHandler),

            # 设置普通Cookie
            (r'/pcookie', index.PcookieHandler),

            # 设置安全Cookie
            (r'/scookie', index.SCookieHandler),
            (r'/gcookie', index.GCookieHandler),

            # Cookie计数
            (r'/cookiecount', index.CookieCountHandler),

            # write and finish 区别
            (r'/MainHandler', index.MainHandler),
            (r'/TesHandler', index.TesHandler),

            # tornado回调函数异步实现
            (r'/students', index.StudentHandler),
            (r'/main', index.StudentsMainHandler),

            # tornado协程实现异步
            (r'/studentsasy', index.StudentsAsyHandler),
            (r'/mainasy', index.MainAsyHandler),

            # tornado网络IO分离
            (r'/studentIO', index.StudentsIoHandler),
            (r'/mainIO', index.MainIoHandler),
        ]

        super(Application, self).__init__(handlers, **config.setting)
        # self.db = SunckMySQL(config.mysql['host'], config.mysql['user'], config.mysql['passwd'], config.mysql['dbName'])