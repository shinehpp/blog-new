import requests
import json

if __name__ == '__main__':
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		'Chrome/77.0.3865.90 Safari/537.36'
	}
	url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
	param = {
		'cname': '',
		'pid': '',
		'keyword': '南京',
		'pageIndex': 1,
		'pageSize': 10,
	}
	response = requests.post(url=url, data=param, headers=headers)
	print(response.json()['Table'][0]['rowcount'])
	if param['pageSize'] < response.json()['Table'][0]['rowcount']:
		param['pageSize'] = response.json()['Table'][0]['rowcount']
		print(type(response.json()['Table'][0]['rowcount']))
		print(param)
		response = requests.post(url=url, data=param, headers=headers)
	print(response.json())
	print(response.status_code)
