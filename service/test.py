from service.base import BaseHanlder, Route
from service.model import Test


@Route.at("/test")
class VideoListService(BaseHanlder):
    def post(self, *args, **kwargs):
        self.resp(0, Test().get_video_list())

