from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import get_all, add, get_first
from webui import downloadProcess
import json

global process
process = None

def download(request):
    global process
    if(process == None):
        return HttpResponseRedirect('/')
    link = request.GET.get('link')
#    print link
    if link != '':
        down_link = add(link)
        if(down_link != None):    
            process.download_link(down_link)
        else:
            return HttpResponse('redown')

    return HttpResponse(down_link)

def check(request):
    global process
    d_json = process.check_stat(request)
    #continue download items in the list
    if(d_json['status'] == 'complete'):
        try:
            link = get_first()
            if(link != ''):
                process.download_link(link)
            else:
                d_json['status'] = 'nomore'
        except:
            d_json['status'] = 'nomore'
    return HttpResponse(json.dumps(d_json), mimetype=u'application/json')

def index(request):
    global process
    
    print user_ip(request)
    
    links = get_all()
    if process == None:
        process = downloadProcess()
#    print links
    #c = {}
    #c.update(csrf(request))
    # 
    r = render_to_response('index.html', {'links': links}, context_instance=RequestContext(request))
    return r

def else_uri(request):
    print user_ip(request)
    return HttpResponse("<html>page not found!!!</html>")
     
def user_ip(request):
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""
    return regip