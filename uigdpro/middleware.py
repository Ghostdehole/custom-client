from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger('django')

class GlobalMaintenanceErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/maintenance/':
            return self.get_response(request)

        response = self.get_response(request)

        if 400 <= response.status_code < 600:
            logger.warning(f"Error {response.status_code} on {request.path}")

            rendered = render(request, 'maintenance.html')
            return HttpResponse(rendered.content, status=response.status_code)


        return response
