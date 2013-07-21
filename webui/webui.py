import sys
import subprocess
import os
import json
import re

from django.http import HttpResponse
from models import pop_link

class downloadProcess:
    
    pipe = None
    isDownloading = False
 
    def download_link(self, link):
        
        if self.isDownloading == False:
            self.isDownloading = True
        elif self.isDownloading == True:
            return 0
        outDir = "K:\\\\home\\downloads\\"
        try:
            path = os.path.join(os.path.dirname(__file__), '../xunlei-lixian/').replace('\\','/')
            self.pipe = subprocess.Popen([sys.executable, '-u', path + "lixian_cli.py", "download", link, "-c", "--output-dir", outDir], 
                                         shell=False, stdout=subprocess.PIPE)
            
        except:
            return -1
    
        return 0
    
    
    def check_stat(self, request):

        if self.pipe == None:
            return HttpResponse(json.dumps({u'per': '0', u'speed': 0, u'eta': '0', u'ok': '3'}), mimetype=u'application/json')
        
        pattern = re.compile(r'(?P<per>\d{1,2})%.*DL:(?P<speed>(\d{1,3}|\d\.\d)\w*)\sETA:(?P<eta>\w*)]')
               
        data = self.pipe.stdout.readline()
        while  data:
            print data
            m = pattern.search(data)
            if m:
                d_json = json.dumps({u'per': m.group('per'), u'speed': m.group('speed'), u'eta': m.group('eta'), u'ok': '0'})
                print d_json
                self.pipe.stdout.flush()
                return HttpResponse(d_json, mimetype=u'application/json')
            elif re.search(r'.*completed\..*', data) != None:  #when the download complete
                self.pipe.stdout.flush()
                self.isDownloading = False
                self.pipe = None
                pop_link()
                return HttpResponse(json.dumps({u'per': '100', u'speed': 0, u'eta': '0', u'ok': '1'}), mimetype=u'application/json')
            else:
                data=self.pipe.stdout.readline()
        
        self.isDownloading = False
        pop_link()
        return HttpResponse(json.dumps({u'per': '0', u'speed': 0, u'eta': '0', u'ok': '2'}), mimetype=u'application/json')
    
    
    def stop_down(self):
        self.pipe.kill();
        
#    m = pattern.search('[#51e64d 1.3GiB/1.5GiB(89%) CN:1 DL:1.5MB ETA:7m3s]')
    
#    print 'regex'
#    print m.group('per')
#    print m.group('speed')
#    print m.group('kb')
#    print m.group('eta')
        
#    return HttpResponseRedirect('/')

#def time(request):

        
        
        
        
        
        
        