import urllib.request as req
import urllib.parse as parse
from django.http import HttpResponse


def index(request):
    url = parse.quote(request.GET.get('url'))
    url = url.replace('%3A', ':')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Firefox/106.0.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    if not url:
        return HttpResponse(status=400)
    try:
        remote_request = req.Request(url, None, headers)
        with req.urlopen(remote_request) as response:
            content = response.read()
    except req.HTTPError as err:
        return HttpResponse('HTTP ERROR ' + url,status=err.code)
    except:
        return HttpResponse('REQUEST ERROR ' + url,status=500)
    return HttpResponse(content, status=200)
