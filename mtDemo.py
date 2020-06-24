# -*- coding: utf-8 -*-
from aliyun_api_gateway_sign_py3.com.aliyun.api.gateway.sdk import client
from aliyun_api_gateway_sign_py3.com.aliyun.api.gateway.sdk.http import request
from aliyun_api_gateway_sign_py3.com.aliyun.api.gateway.sdk.common import constant

host = "https://api.medofmind.com"
url = "/nlp/translateText"

cli = client.DefaultClient(app_key="<TODO>", app_secret="<TODO>")

import json, collections
req_post = request.Request(host=host, protocol=constant.HTTPS, url=url, method="POST", time_out=30000)
body = collections.OrderedDict()
body["fromLang"] = "en"
body["toLang"] = "zh_CN"
body["text"] = "Older adults and people who have severe underlying medical conditions like heart or lung disease or diabetes seem to be at higher risk for developing serious complications from COVID-19 illness."

#both json string or bytes works 
#req_post.set_body(json.dumps(body))
req_post.set_body(bytes(json.dumps(body), encoding="utf8"))
req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
status, header, body = cli.execute(req_post)
print("http code: ", status)
print("header: ", header)
print("body: ", body)
