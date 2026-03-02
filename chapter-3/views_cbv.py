from django.views import View
from django.http import JsonResponse
from django.utils import timezone


class HealthCheckView(View):
    """
    Simple class-based view to check if server is running.
    """

    def get(self, request, *args, **kwargs):
        data = {
            "status": "success",
            "message": "Server is running properly",
            "timestamp": timezone.now(),
        }
        return JsonResponse(data)


class TextAnalysisView(View):
    """
    Class-based view for basic text analysis.
    """

    def post(self, request, *args, **kwargs):
        text = request.POST.get("text", "")

        response_data = {
            "word_count": len(text.split()),
            "character_count": len(text),
            "uppercase": text.upper(),
        }

        return JsonResponse(response_data)
