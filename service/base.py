import json
import tornado.web

from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor


class BaseHanlder(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(100)

    def prepare(self):
        self.input = json.loads(self.request.body) if self.request.body else {}
        self.set_headers()

    def set_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET")

    def post(self, *args, **kwargs):
        self.send_error(404)

    def get(self, *args, **kwargs):
        self.send_error(404)

    def resp(self, status, data):
        self.write({
            "data": data,
            "status": status
        })


class Route(object):
    executor = ThreadPoolExecutor(100)
    ROUTES = []

    @staticmethod
    def at(route):
        def add_route(handler):
            handler.post = run_on_executor(handler.post)
            handler.get = run_on_executor(handler.get)
            Route.ROUTES.append((route, handler))
        return add_route

    @staticmethod
    def get_route():
        print(Route.ROUTES)
        return Route.ROUTES
