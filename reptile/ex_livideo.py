import requests
import aiohttp
import asyncio
import re
import time
from lxml import html


headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		'Chrome/77.0.3865.90 Safari/537.36'
}
head_url = 'https://www.pearvideo.com/'
head_text = requests.get(url=head_url,headers=headers).text
tree = html.etree.HTML(head_text)
a_list = tree.xpath('//div[@id="vervideoTlist"]//ul//a')
urls = []
for a in a_list:
	v_name = a.xpath('.//div[@class="vervideo-name"]/text()')[0]+'.mp4'
	v_url = head_url+a.xpath('./@href')[0]
	v_url_text = requests.get(url=v_url,headers=headers).text

	video_url = re.findall('https://video.pearvideo.com/mp4(.*?)"', v_url_text, re.S)[0]
	urls.append({
		'name': v_name,
		'url': str('https://video.pearvideo.com/mp4'+video_url)
	})
print(urls)


async def get_video(url, name):
	print(name, '开始下载。。。')
	async with aiohttp.ClientSession() as session:
		async with await session.get(url=url,headers=headers) as response:
			video_content = await response.read()
			with open(name[-8:], 'wb') as f:
				f.write(video_content)
			print(name, '下载完成。。。')
			return video_content

s_time = time.time()
task_list = []
for i in urls:
	c = get_video(i['url'], i['name'])
	task = asyncio.ensure_future(c)
	task_list.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task_list))
end_time = time.time()
print(end_time-s_time)