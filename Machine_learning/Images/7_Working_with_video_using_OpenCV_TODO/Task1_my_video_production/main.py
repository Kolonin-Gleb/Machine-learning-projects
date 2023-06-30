import cv2
from PIL import Image, ImageEnhance
import numpy as np

# Делаем изображение черно-белым
def add_mono(img):
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
	return img


# Накладываем логотип
def add_logo(img):
	# Переводим массив изображения в объект Pillow и преобразуем в тип RGBA с маской прозрачности
	img_out = Image.fromarray(img)

	l = logo.copy()
	alpha = ImageEnhance.Brightness(l.split()[3]).enhance(opacity_logo)
	l.putalpha(alpha)

	img_out.paste(logo, (540, 15), l)

	return np.asarray(img_out, dtype='uint8')


# Накладываем подпись
def add_caption(img):
	# Переводим массив изображения в объект Pillow и преобразуем в тип RGBA с маской прозрачности
	img_out = Image.fromarray(img)

	global opacity_caption
	global isCaption
	global captionTimer

	# print(captionTimer)

	if (captionTimer < 50) and (opacity_caption < 1):
		opacity_caption += 0.04

	if captionTimer > 80:
		if opacity_caption > 0:
			opacity_caption -= 0.04
		else:
			isCaption = False

	cap = caption.copy()
	alpha = ImageEnhance.Brightness(cap.split()[3]).enhance(opacity_caption)
	cap.putalpha(alpha)

	img_out.paste(caption, (0, 380), cap)

	captionTimer += 1

	return np.asarray(img_out, dtype='uint8')

frame = cv2.VideoCapture(0)

# Стутусы отображения
isLogo = False
isCaption = False

# Счетчик времени для подписи
captionTimer = 0

# Уровни прозрачности
opacity_logo = 1
opacity_caption = 1

# Загружаем картинки
caption_img = cv2.imread('Gleb_caption.png', cv2.IMREAD_UNCHANGED)
logo_img = cv2.imread('IT_Club_logo.png', cv2.IMREAD_UNCHANGED)

# Переводим массивы в объекты Pillow
logo = Image.fromarray(logo_img)
caption = Image.fromarray(caption_img)

# Обрабатываем кадры в цикле
while True:
	status, image = frame.read()

	if isLogo:
		image = add_logo(image)

	if isCaption:
		image = add_caption(image)

	# Отображаем фрэйм с видео-трансляцией
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

	# Обрабатываем нажатие клавиши c, которая включает или отключает подпись
	if k == 99:
		if not isCaption:
			isCaption = True
			captionTimer = 0
			opacity_caption = 0

frame.release()
cv2.destroyAllWindows()
