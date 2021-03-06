import requests as req
import json
from flask import Flask, current_app,g


REG_URL = 'http://10.100.100.130:6001/v2/'
#REG_URL = 'http://10.20.60.3:6001/v2'


def get_repos():
    #import pdb; pdb.set_trace()
    url = REG_URL + '_catalog'
    res = req.get(url)
    return res

def get_tags(img_path):
    url = REG_URL + img_path + '/tags/list'
    res = req.get(url)
    return res

def get_tag_info(img_path,tag):
    url = REG_URL + img_path + '/manifests/' + tag
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
    return res.headers.get('Docker-Content-Digest')


def del_img(img_path,digest):
    url = REG_URL + img_path + '/manifests/' + digest
    res = req.delete(url)
    return res
