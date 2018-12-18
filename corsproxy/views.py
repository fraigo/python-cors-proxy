import urllib.request as req
from django.http import HttpResponse


def index(request):
    url = request.GET.get('url')
    if not url:
        return HttpResponse(status=400)
    with req.urlopen(url) as response:
        content = response.read()
    return HttpResponse(content, status=200)
