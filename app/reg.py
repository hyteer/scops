import requests as req
import json

#REG_URL = 'http://10.100.100.130:6001/v2'
REG_URL = 'http://10.20.60.3:6001/v2'

def get_repos():
    url = REG_URL + '/_catalog'
    res = req.get(url)
    return res

def get_tags(img_path):
    url = REG_URL + img_path + '/tags/list'
    res = req.get(url)
    return res

def get_manifest(img_path,tag):
    headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
    url = REG_URL + img_path + '/manifests/' + tag
    res = req.get(url,headers=headers)
    #import pdb; pdb.set_trace()
    return res

def get_digest(img_path,tag):
    headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
    url = REG_URL + img_path + '/manifests/' + tag
    res = req.get(url,headers=headers)
    #import pdb; pdb.set_trace()
    return res.headers['Docker-Content-Digest']

def del_tag(img_path,digest):
    url = REG_URL + img_path + '/manifests/' + digest
    res = req.delete(url)
    return res
