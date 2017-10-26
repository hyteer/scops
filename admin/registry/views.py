from flask import jsonify, url_for, request
import json
from registry import reg
from registry import api


@reg.route('/')
def api_index():
    return jsonify({'desc':'registry api...'})

@reg.route('/test')
def test():
    return jsonify({'desc':'apitest...'})

# docker registry

# 获取仓库列表
@reg.route('/repos')
def reg_repos():
    res1 = api.get_repos()
    print("Repos: ", res1.text)
    return res1.text

# 获取Tags列表
@reg.route('/tags')
def reg_tags():
    #import pdb; pdb.set_trace()
    img = request.args.get('img')
    r = api.get_tags(img)
    #r = api.get_tags('opt/dev/frontend-h5-dinner')
    print("Tags: ", r)
    return r.text

# 获取Tags列表-sorted
@reg.route('/sorted-tags')
def reg_sorted_tags():
    img = request.args.get('img')
    r_tags = api.get_tags(img)
    print("Tags:",r_tags)
    _tags = json.loads(r_tags.text)['tags']
    tlist = []
    tdict = {}
    for tag in _tags:
        r = api.get_tag_info(img,tag)
        dt = json.loads(r.text)
        last = dt['history'][0]['v1Compatibility']
        lastdt = json.loads(last)
        tdict.update({tag:lastdt['created']})
    #import pdb; pdb.set_trace()
    sd = sorted(tdict.items(), key=lambda tdict:tdict[1])
    for i in range(len(sd)):
        tlist.append(sd[i][0])
    print("TagsInfo: ", tlist)
    return jsonify(tlist)

# 批量获取Tags信息
@reg.route('/tags-info')
def reg_tags_info():
    img = request.args.get('img')
    r_tags = api.get_tags(img)
    print("Tags:",r_tags)
    _tags = json.loads(r_tags.text)['tags']
    tlist= []
    for tag in _tags:
        _info = {'name':tag}
        r = api.get_tag_info(img,tag)
        dt = json.loads(r.text)
        last = dt['history'][0]['v1Compatibility']
        lastdt = json.loads(last)
        _info['created'] = lastdt['created']
        _info['os'] = lastdt['os']
        _info['docker_version'] = lastdt['docker_version']
        tlist.append(_info)
    print("TagsInfo: ", tlist)
    return jsonify(tlist)

@reg.route('/manifest')
def reg_manifest():
    r = api.get_manifest('/debug','dinner')
    print("Repos: ", r)
    return r.text

# 获取Tag信息
@reg.route('/tag-info')
def reg_tag_info():
    r = api.get_tag_info('/debug','dinner')
    js = json.loads(r.text)
    last = js['history'][0]['v1Compatibility']
    js2 = json.loads(last)
    print("Created:",js2['created'])
    #print("TagInfo: ", last)
    return jsonify(js2)

# 获取digest值
@reg.route('/digest')
def reg_digest():
    r = api.get_digest('/debug','dinner')
    print("Digest: ", r)
    return jsonify(r)

# 删除镜像-old
@reg.route('/del-img-old',methods=['DELETE', 'POST'])
def reg_del_img_old():
    digest = api.get_digest('/debug','dinner')
    print("Digest:",digest)
    if digest:
        r = api.del_img('/debug', digest)
        print("ResCode: ", r.status_code)
        return "ResCode: %s" % r.status_code
    else:
        return "image not exist..."

# 删除镜像
@reg.route('/del-img',methods=['DELETE', 'POST'])
def reg_del_img():
    #import pdb; pdb.set_trace()
    #data = request.get_data().decode('utf-8')
    #tags = json.loads(data)
    #import pdb; pdb.set_trace()
    img = request.json['img']
    tags = request.json['tags']
    print("Img:%s, Tags:%s" % (img,tags))

    #tags = ['dinner','1025']
    tagsdict = {}
    for tag in tags:
        digest = api.get_digest(img,tag)
        #import pdb; pdb.set_trace()
        print("Digest:",digest)
        if digest:
            r = api.del_img(img, digest)
            tagsdict.update({tag:r.status_code})
    print("ResDict: ", tagsdict)
    return jsonify(tagsdict)

# 删除镜像 v2
@reg.route('/del-img-v2',methods=['DELETE', 'POST'])
def reg_del_img_v2():
    #import pdb; pdb.set_trace()
    #data = request.get_data().decode('utf-8')
    #tags = json.loads(data)
    #import pdb; pdb.set_trace()
    img = request.json['img']
    tags = request.json['tags']
    print("Img:%s, Tags:%s" % (img,tags))

    #tags = ['dinner','1025']
    tagsdict = {}
    for tag in tags:
        digest = api.get_digest(img,tag)
        #import pdb; pdb.set_trace()
        print("Digest:",digest)
        if digest:
            r = api.del_img(img, digest)
            tagsdict.update({tag:r.status_code})
    print("ResDict: ", tagsdict)
    return jsonify(tagsdict)


#
