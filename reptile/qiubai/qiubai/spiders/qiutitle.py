# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class QiutitleSpider(scrapy.Spider):
	name = 'qiutitle'
	# allowed_domains = ['www.xxx.com']
	start_urls = ['http://jandan.net/']

	def parse(self, response):
		div_list = response.xpath('//div[@class="post f list-post"]')
		item = QiubaiItem()
		for div in div_list:
			title_name = div.xpath('.//div[2]/h2//text()').extract_first()
			title_tag = ''.join(div.xpath('.//div[2]/div[@class="time_s"]//text()').extract())
			item['title'] = title_name
			item['tag'] = title_tag
			yield item
