# -*- coding: utf-8 -*-
import requests
import sys
import json
import os

url = "http://jsondata.25pp.com/index.html"
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko)"
referer = "http://jsondata.25pp.com/index.html?tunnel-command=4261421120"
cookie = {}
list = []
word = ''
def crawl(keyword):
	if keyword is not word:
		list = []
	if not keyword:
		raise(KeyError,'请输入app 名')
	page = 0
	while True:
		# 需要对参数做一次 utf8 编码
		n = ('''{"dcType":0, "keyword":"%s", "clFlag":1, "perCount":15, "page":%d}'''%(keyword, page)).encode("utf-8")
		headers = {"User-Agent":ua, "Referer":referer, "Tunnel-Command":"4262469664", "Origin":"http://jsondata.25pp.com", "Connection":"keep-alive", "Content-Type":"application/x-www-form-urlencoded", "Accept-Language":"en-us", "Content-Type":"application/x-www-form-urlencoded"}
		res = requests.post(url, data=n, headers = headers, cookies=cookie)
		page = page + 1
		if res.status_code==200:
			text = res.text
			if text.startswith(u'\ufeff'):
				text = text.encode('utf8')[3:].decode('utf8')
			j = json.loads(text)
			items = j['content']
			for n, item in enumerate(items):
				print(str(n + len(list))+'.',item["title"], '版本号:'+item["version"], '下载地址:'+item['downurl'])
			list = list+items
		else:
			break
		print('如果不存在请输入n:')
		a = input('')
		if a == 'n':
			pass
		else:
			exit(0)
		# 	try:
		# 		b = int(a)
		# 	except ValueError as e:
		# 		print('请输入数字! 我退出了')
		# 	path = os.getcwd()
		# 	ipaPath = os.path.join(path, list[b]['title']+'.ipa')
		# 	print('curl -o ' + keyword+'.ipa '+ list[b]['downurl'])
		# 	os.popen('curl ' + '-A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"' +'-o ' + keyword +'.ipa '+ list[b]['downurl'])	
			
if __name__ == '__main__':
	print(sys.argv)
	if len(sys.argv) == 2:
		crawl(sys.argv[1])
	else:
		raise(KeyError,'请输入app 名')