# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaiPipeline(object):
	f = None

	def open_spider(self, spider):
		self.f = open('111.txt', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		self.f.write(item['title'])
		self.f.write(item['tag'])
		return item

	def close_spider(self,spider):
		self.f.close()

class QiubaiPipeline2(object):
	f = None

	def open_spider(self, spider):
		self.f = open('222.txt', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		self.f.write(item['title']+'\n')
		self.f.write(item['tag']+'\n\n')
		return item

	def close_spider(self,spider):
		self.f.close()