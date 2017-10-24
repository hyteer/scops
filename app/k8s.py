import requests as req
import json

API_URL = 'http://10.100.100.142:8080/api/v1'
RESP_TPL = {'code':200,'msg':'success','data':''}

def res():
    res = req.get(API_URL)
    return res

def nodes():
    url = API_URL + '/nodes'
    res = req.get(url)
    resp = RESP_TPL
    data = []
    #import pdb; pdb.set_trace()
    js = json.loads(res.text)
    for i in range(0,len(js['items'])):
        dt = {}
        dt['name'] = js['items'][i]['metadata']['name']
        dt['mem'] = js['items'][i]['status']['capacity']['memory']
        dt['pods'] = js['items'][i]['status']['capacity']['pods']
        data.append(dt)
    #import pdb; pdb.set_trace()
    resp.update({'data':data})
    return resp

def namespaces():
    url = API_URL + '/namespaces'
    res = req.get(url)
    return res

def get_manifest(img_path,tag):
    headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
    url = REG_URL + img_path + '/manifests/' + tag
    res = req.get(url,headers=headers)
    return res

def del_tag(img_path,digest):
    url = REG_URL + img_path + '/manifests/' + digest
    res = req.delete(url)
    return res
