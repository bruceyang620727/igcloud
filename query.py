import json
import time
import urllib.request

def start(instagramID):
    max_id=''
    IGcontent=''
    cc_count=0
    url_host='https://www.instagram.com/'
    url_path = str(instagramID)+'/?__a=1&max_id='

    try:
        check = urllib.request.urlopen(url_host+url_path+max_id)
    except Exception as Q:
        try:
            if(int(Q.getcode()/100)==4):
                print('User not found')
        except:
            print('Please check your network status')
        exit()

    while 1:
        try:
            url = url_host+url_path+max_id
            request = urllib.request.Request(url=url)
            response = urllib.request.urlopen(request,timeout=5)
            res_body = response.read()
            j=json.loads(res_body.decode("utf-8"))
            if j['user']['is_private'] != True:
                items=j['user']['media']['nodes']
                for i in items:
                    if 'caption' in i:
                        IGcontent+=str(i['caption'])
            else:
                print('This user is private! Sorry!')
                exit()

            max_id = items[len(items)-1]['id']
            if j['user']['media']['page_info']['has_next_page']==True:
                cc_count+=len(items)
                stdout = '('
                stdout += str(int(cc_count/j['user']['media']['count']*100))
                stdout +='%)'

                stdout += ' Now query '+str(cc_count)+' posts '
                print(stdout)
            else:
                print('100%! Wait for rendering')
                return IGcontent
        except Exception as Q:
            print(Q)
            print('Time out? Wait 10 seconds (Use Ctrl-c to KeyboardInterrupt)')
            time.sleep(10)