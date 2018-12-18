from django.http import HttpResponse


class Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (request.method == "OPTIONS"):
            return HttpResponse("OPTIONS")
        response['Access-Control-Allow-Origin'] = "*"
        return response
