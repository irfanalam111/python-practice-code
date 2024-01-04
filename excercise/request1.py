import requests
import sys
import json

if len(sys.argv)!=2:
    sys.exit()

class request:
    def __init__(self,url : str):
        self.url=url

    def get_(self):
        self.response_get=requests.get(self.url)
        clean=json.dumps(self.response_get.json())
        return clean
    
    def head_(self):
        self.response_head=requests.head(self.url)
        clean=json.dumps(self.response_head.json())
        return clean
    


if __name__=='__main__':
    obj=request()
    print(obj.get_("https://api.github.com"))

        
