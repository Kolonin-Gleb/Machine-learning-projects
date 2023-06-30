#
# Отображаем видео с веб-камеры
#

import cv2

frame = cv2.VideoCapture(1)

while True:
	status, image = frame.read()

	cv2.imshow("TV show", image)

	k = cv2.waitKey(30)
	if k == 27:
		break

frame.release()
cv2.destroyAllWindows()