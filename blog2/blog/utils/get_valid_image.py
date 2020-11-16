from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random


def get_color():
	return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_text():
	upper_letter = chr(random.randint(65, 90))
	num = chr(random.randint(48,57))
	lower_letter = chr(random.randint(97, 122))
	choice = random.choice([upper_letter, num, lower_letter])
	return choice


def get_image(request):
	img = Image.new('RGB',(270, 40), color=get_color())
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('/statics/Gabriola.ttf', size=35)
	code = ''
	for i in range(6):
		draw.text((i*40+30, 5), get_text(), get_color(), font=font)
		code += get_text()
	print(code)
	request.session['code'] = code
	f = BytesIO()
	img.save(f, 'png')
	data = f.getvalue()
	return data
