from flask import jsonify, url_for
import json
from regitry import reg
from flask import Module
api = Module(__name__)

@api.route('/')
def api_index():
    return jsonify({'desc':'api...'})

@api.route('/test')
def test():
    return jsonify({'desc':'apitest...'})

# docker registry

# 获取仓库列表
@api.route('/reg/repos')
def reg_repos():
    res1 = reg.get_repos()
    print("Repos: ", res1.text)
    return res1.text

# 获取Tags列表
@api.route('/reg/tags')
def reg_tags():
    r = reg.get_tags('/debug','dinner')
    print("Tags: ", r)
    return r.text

# 批量获取Tags信息
@api.route('/reg/tags-info')
def reg_tags_info():
    r_tags = reg.get_tags('/debug')
    print("Tags:",r_tags)
    _tags = json.loads(r_tags.text)['tags']
    tlist= []
    for tag in _tags:
        _info = {'name':tag}
        r = reg.get_tag_info('/debug',tag)
        js = json.loads(r.text)
        last = js['history'][0]['v1Compatibility']
        lastjs = json.loads(last)
        _info['created'] = lastjs['created']
        _info['os'] = lastjs['os']
        _info['docker_version'] = lastjs['docker_version']
        tlist.append(_info)
    print("TagsInfo: ", tlist)
    return jsonify(tlist)

@api.route('/reg/manifest')
def reg_manifest():
    r = reg.get_manifest('/debug','dinner')
    print("Repos: ", r)
    return r.text

# 获取Tag信息
@api.route('/reg/tag-info')
def reg_tag_info():
    r = reg.get_tag_info('/debug','dinner')
    js = json.loads(r.text)
    last = js['history'][0]['v1Compatibility']
    js2 = json.loads(last)
    print("Created:",js2['created'])
    #print("TagInfo: ", last)
    return jsonify(js2)

# 获取digest值
@api.route('/reg/digest')
def reg_digest():
    r = reg.get_digest('/debug','dinner')
    print("Digest: ", r)
    return jsonify(r)

# 删除镜像
@api.route('/reg/del-img',methods=['DELETE', 'POST'])
def reg_del_img():
    digest = reg.get_digest('/debug','dinner')
    #import pdb; pdb.set_trace()
    print("Digest:",digest)
    if digest:
        r = reg.del_img('/debug', digest)
        print("ResCode: ", r.status_code)
        return "ResCode: %s" % r.status_code
    else:
        return "image not exist..."

# 批量删除镜像
@api.route('/reg/batch-del-img',methods=['DELETE', 'POST'])
def reg_batch_del_img():
    tags = ['dinner','1025']
    tagsdict = {}
    for tag in tags:
        digest = reg.get_digest('/debug',tag)
        #import pdb; pdb.set_trace()
        print("Digest:",digest)
        if digest:
            r = reg.del_img('/debug', digest)
            tagsdict.update({tag:r.status_code})
    print("ResDict: ", tagsdict)
    return jsonify(tagsdict)
