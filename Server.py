import subprocess,os
from bottle import run, post, request, response, get, route,auth_basic


subprocess.Popen(["autossh","-M","0","-R","443:****:****","****"],stdout=subprocess.PIPE)

def check(user,pw):
## Add Signature for protection
    if user == "******" and pw == "******":
        return True
    else:
        return False

@route('/',method="GET")
def index():
    return ""

@route('/***',method = 'GET')
@auth_basic(check)
def process():
    final = {}
    get_val = request.params.get('url')
    if get_val is not None:
        json_val = subprocess.check_output(['go run dnsgrep.go -f fdns_a.sort.txt -i "'+str(get_val)+'"'],shell=True)
        json_val = json_val.decode().strip('\n').split('\n')
        final['results'] = json_val
        # for each_val in json_val:
        #     print(each_val.split(','))
        #print(json_val)
        return final
