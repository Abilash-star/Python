"""Collect Json objects and sort them in order with a list of strings for User Names"""    
    
import urllib.request as url_data
import json
import pprint

with url_data.urlopen("http://api.open-notify.org/astros.json") as resp_obj:
    if resp_obj.getcode() == 200:
        src_data = resp_obj.read().decode("utf-8")
        _json = json.loads(src_data)
        obj_convert = [i["name"] for i in _json["people"]]
        data = sorted(sort_data for sort_data in obj_convert)
        print(data)
    else:
        print("Http Error:", resp_obj.getcode())   
