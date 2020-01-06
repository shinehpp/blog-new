import requests
from lxml import html

if __name__ == '__main__':
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		'Chrome/77.0.3865.90 Safari/537.36'
	}
	url_head = 'https://www.58.com/ershoufang/'
	head_text = requests.get(url=url_head, headers=headers).text
	tree = html.etree.HTML(head_text)
	a_list = tree.xpath('//tr/td[@class="t"]')
	print(a_list)
	for a in a_list:
		title = a.xpath('.//a/text()')[0]
		content_url = a.xpath('.//a/@href')[0]
		content_url = 'https:' + content_url
		content = requests.get(url=content_url,headers=headers).text
		content_etree = html.etree.HTML(content)
		price = content_etree.xpath('//p[@class="house-basic-item1"]/span[1]/text()')
		print(price)