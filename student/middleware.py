import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        return
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        responce = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return responce
    def process_exception(self, request):
        pass
    def process_template_responce(self, request, responce):
        return responce
    def process_responce(self, request, responce):
        costed = time.time() - self.start_time
        print('request to responce cose: {:.2f}s'.format(costed))
        return responce
