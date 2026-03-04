import time
from django.utils.deprecation import MiddlewareMixin


class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Custom middleware to log request details
    and execution time.
    """

    def process_request(self, request):
        request.start_time = time.time()
        print(f"[REQUEST START] Path: {request.path} | Method: {request.method}")

    def process_response(self, request, response):
        if hasattr(request, "start_time"):
            duration = time.time() - request.start_time
            print(
                f"[REQUEST END] Path: {request.path} | "
                f"Status: {response.status_code} | "
                f"Duration: {duration:.4f}s"
            )
        return response
