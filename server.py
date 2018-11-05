from tornado.web import RequestHandler

import tornado.web
import tornado.httpserver
import tornado.ioloop
import config
from views import index
from application import Application

if __name__ == "__main__":
    app = Application()

    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(config.options['port'])
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
