from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import get_all, add, get_first
from webui import downloadProcess

global process
process = None

def download(request):
    global process
    link = request.GET.get('link')
#    print link
    if link != '':
        if(add(link) == 0):    
            process.download_link(link)
        else:
            return HttpResponse('redown')
    else:
        link = get_first()
        if(link != ''):
            process.download_link(link)
    return HttpResponse(link)

def check(request):
    global process
    return process.check_stat(request)

def index(request):
    global process
    links = get_all()
    if process == None:
        process = downloadProcess()
#    print links
    return render_to_response('index.html', {'links': links}, context_instance=RequestContext(request))
