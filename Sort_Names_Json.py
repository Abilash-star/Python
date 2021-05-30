"""Collect Json objects and sort them in order with a list of strings for User Names"""    
    
import urllib.request as url_data
import json

with url_data.urlopen("http://api.open-notify.org/astros.json") as resp_obj:
    if resp_obj.getcode() == 200:
        src_data = resp_obj.read()
        _json = json.loads(src_data)
        for i in _json["people"]:
            print(i["name"])
    else:
        print("Http Error:", resp_obj.getcode())    
