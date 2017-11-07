import json
from registry import api
from registry.config import KEEP_COPIES,SRV_MAP

def get_sorted_tags(img):
    print('Call Img:',img)
    tlist = []
    tdict = {}
    r = api.get_tags(img)
    rd = json.loads(r.text)
    if rd.get('errors'):
        print("img %s not exist..." % img)
        return tlist
    _tags = rd['tags']
    print("Tags:", _tags)
    if _tags:
        for tag in _tags:
            #print("img:%s,_tag:%s" % (img,tag))
            try:
                r = api.get_tag_info(img,tag)
                dt = json.loads(r.text)
                last = dt['history'][0]['v1Compatibility']
                lastdt = json.loads(last)
                tdict.update({tag:lastdt['created']})
            except KeyError:
                print("This tag is broken...")

            continue
    #import pdb; pdb.set_trace()
    sd = sorted(tdict.items(), key=lambda tdict:tdict[1])
    if len(sd) > KEEP_COPIES:
        for i in range(len(sd)-KEEP_COPIES):
            #print(sd[i][0])
            if sd[i][0] != 'debug':
                tlist.append(sd[i][0])
    #print("TagsInfo: ", tlist)
    return tlist

def del_img(img,tags):
    tagsdict = {}
    for tag in tags:
        digest = api.get_digest(img,tag)
        #import pdb; pdb.set_trace()
        print("Digest:",digest)
        if digest:
            r = api.del_img(img, digest)
            tagsdict.update({tag:r.status_code})
    print("ResDict: ", tagsdict)
    return tagsdict

def get_env_img_tags(env):
    lst = []
    for srv in SRV_MAP['service']:
        _img = "opt/%s/%s" % (env,srv)
        print("_img:",_img)
        _tags = get_sorted_tags(_img)
        if _tags:
            lst.append([_img,_tags])
    return lst
