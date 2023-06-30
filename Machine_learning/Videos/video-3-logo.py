import cv2
from PIL import Image, ImageEnhance
import numpy as np

frame = cv2.VideoCapture(1)

isColor = True
isLogo = False

opacity_logo = 1

# Загружаем логотип
logo_img = cv2.imread('logo-rgba.png', cv2.IMREAD_UNCHANGED)

# Переводим массив в объект Pillow
logo = Image.fromarray(logo_img)


# Делаем изображение черно-белым
def add_mono(img):
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
	return img


# Накладываем логотип
def add_logo(img):
	# Переводим массив изображения в объект Pillow и преобразуем в тип RGBA с маской прозрачности
	im = Image.fromarray(img)
	im = im.convert('RGBA')

	img_out = im.copy()

	l = logo.copy()
	alpha = ImageEnhance.Brightness(l.split()[3]).enhance(opacity_logo)
	l.putalpha(alpha)

	img_out.paste(logo, (540, 15), l)

	return np.asarray(img_out, dtype='uint8')


# Обрабатываем кадры в цикле
while True:
	status, image = frame.read()

	if not isColor:
		image = add_mono(image)

	if isLogo:
		image = add_logo(image)

	cv2.imshow("TV show", image)
	
	k = cv2.waitKey(30)

	# Обрабатываем нажатие клавиши Esc для выхода
	if k == 27:
		break

	# Обрабатываем нажатие клавиши l, которая включает или отключает логотип
	if k == 108:
		if isLogo:
			isLogo = False
		else:
			isLogo = True

	# Обрабатываем нажатие клавиши b, которая включает или отключает цветность
	if k == 98:
		if isColor:
			isColor = False
		else:
			isColor = True

	# Обрабатываем нажатие клавиши -, которая уменьшает прозрачность лого
	if k == 45:
		if opacity_logo > 0:
			opacity_logo -= 0.1

	# Обрабатываем нажатие клавиши +, которая уменьшает прозрачность лого
	if k == 43:
		if opacity_logo < 1:
			opacity_logo += 0.1

frame.release()
cv2.destroyAllWindows()




