
import requests
import json

class AutoDownload(object):
    uri = ''
    headers = {"Content-Type":"application/json"}
    
    def __init__(self, uri='http://tv.xdream.info/download/'):
        self.uri = uri

    def get_updates(self):
        data = json.dumps({"email":"gymgunner@gmail.com"})

        r = requests.get(self.uri, data=data, headers=self.headers)
        
        if(r.status_code == 200):
            updates = json.loads(r.text)
        else:
            updates = []

        return updates
        
    def post_download_status(self):
        pass

