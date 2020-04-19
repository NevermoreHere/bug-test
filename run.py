import tornado.ioloop
import tornado.web

from service.base import Route, BaseHanlder


def make_app():
    setting = {'debug': True, "default_handler_class": BaseHanlder}
    return tornado.web.Application(handlers=Route.get_route(), **setting)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
