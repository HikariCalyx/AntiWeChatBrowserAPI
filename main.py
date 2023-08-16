#!/usr/bin/python3
# Anti WeChat and Mobile Browser API
# 2015-2023 (C) Hikari Calyx Tech. All Rights Reserved.
from flask import Flask, request, redirect, render_template
from gevent import pywsgi

# Configurations
auth_port = 443
copyright_string = '2015-2023 (C) Your Company or Organization Name. All Rights Reserved. '
app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


def check_useragent(useragent):
    if 'WindowsWechat' in useragent:
        return 'anti-wechat-pc.html'
    elif 'MacWechat' in useragent:
        return 'anti-wechat-mac.html'
    elif 'MicroMessenger' in useragent:
        return 'anti-wechat-phone.html'
    elif 'Android ' in useragent or 'iPhone OS' in useragent or 'Windows Phone' in useragent or 'Mobile' in useragent:
        return 'anti-phone.html'
    else:
        return None


############### CowTransfer Download Anti-WeChat Method ###############
app.route('/FileDownload/CTWorks', methods=['GET'])


def ctworks():
    CTID = request.args.get('id', type=str, default='Unknown')
    ua = request.headers.get('User-Agent', type=str, default='Unknown')
    allowmobile = request.args.get('allowmobile', type=str, default='0')
    cturl = 'https://cowtransfer.com/s/' + CTID
    if check_useragent(useragent=ua) and str(allowmobile) == '0':
        return render_template(check_useragent(useragent=ua),
                               copyrightstring=copyright_string,
                               useragent=ua,
                               cturl=cturl)
    else:
        return redirect(cturl)


server = pywsgi.WSGIServer(('0.0.0.0', auth_port),
                           app,
                           certfile='/etc/letsencrypt/live/yourdomain.com/fullchain.pem',
                           keyfile='/etc/letsencrypt/live/yourdomain.com/privkey.pem')
print("Now listening on Port " + str(auth_port))
server.serve_forever()
