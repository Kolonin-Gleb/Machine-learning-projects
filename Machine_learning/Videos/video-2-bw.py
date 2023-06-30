#
# Управляем цветностью видео
#

import cv2

frame = cv2.VideoCapture(1)

isColor = True


# Делаем изображение черно-белым
def add_mono(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	return img


# Обрабатываем кадры в цикле
while True:
	status, image = frame.read()

	if not isColor:
		image = add_mono(image)

	cv2.imshow("TV show", image)

	k = cv2.waitKey(30)

	# Обрабатываем нажатие клавиши Esc для выхода
	if k == 27:
		break

	# Обрабатываем нажатие клавиши b, которая включает или отключает цветность
	if k == 98:
		if isColor:
			isColor = False
		else:
			isColor = True

frame.release()
cv2.destroyAllWindows()
