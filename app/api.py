from flask import jsonify, url_for
from main import app
import reg, k8s


@app.route('/api')
def api_index():
    return jsonify({'desc':'api...'})

@app.route('/api/test')
def test():
    return jsonify({'desc':'apitest...'})

# docker registry

@app.route('/api/reg/repos')
def reg_repos():
    # list repos
    res1 = reg.get_repos()
    print("Repos: ", res1.text)
    return res1.text

@app.route('/api/reg/manifest')
def reg_manifest():
    # list repos
    r = reg.get_manifest('/debug','dinner')
    print("Repos: ", r)
    return r.text

@app.route('/api/reg/digest')
def reg_digest():
    # list repos
    r = reg.get_digest('/debug','dinner')
    print("Digest: ", r)
    return r

@app.route('/api/reg/dinner')
def reg_digest():
    # list repos
    r = reg.get_digest('/debug','dinner')
    print("Digest: ", r)
    return r


# k8s

@app.route('/api/k8s/res')
def res_list():
    # list repos
    r = k8s.res()
    print("Resources: ", r.text)
    return r.text

@app.route('/api/k8s/nodes')
def node_list():
    # list repos
    r = k8s.nodes()
    #import pdb; pdb.set_trace()
    print("Resources: ", r)
    return jsonify(r)
