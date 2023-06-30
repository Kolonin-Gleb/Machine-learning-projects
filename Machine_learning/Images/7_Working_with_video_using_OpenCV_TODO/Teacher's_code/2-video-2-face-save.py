from PIL import Image, ImageEnhance
import sys
import numpy as np
import cv2
import math
import os
import shutil  # Библиотека для работы с файлами
import glob    # Расширение для использования Unix обозначений при задании пути к файлу

record_icon_img = cv2.imread('record-icon.png', cv2.IMREAD_UNCHANGED)
record_icon = Image.fromarray(record_icon_img)

isRecord = False
# Тут будет храниться номер кадра
file_counter = 0
# Директория для записи кадров
videoDir = 'video'


# Получаем кадр с видеокамеры
frame = cv2.VideoCapture(1)

# Создаем объект для обнаружения лица
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Накладываем значок индикатора записи
def add_record(img):
	# Переводим массив изображения в объект Pillow и преобразуем в тип RGBA с маской прозрачности
	img_out = Image.fromarray(img)

	img_out.paste(record_icon, (20, 420), record_icon)

	return np.asarray(img_out, dtype='uint8')


# Начинаем запись
def start_recording():
	global file_counter

	if os.path.isdir(videoDir):
		shutil.rmtree(videoDir+'/')  # удаляем каталог вместе с содержимым

	os.mkdir(videoDir)
	file_counter = 0


# Заканчиваем запись
def stop_recording():
	if os.path.isdir(videoDir):
		gif_name = 'second_video.gif'
		video_name = 'second_video.mp4'
		fps = 60

		files = glob.glob(videoDir + '/*.png')
		files.sort()

		file_list = []
		for i in files:
			for j in range(4):
				file_list.append(i)


def save_frame(img):
	global file_counter

	file_name = "%05d" % file_counter
	cv2.imwrite(videoDir+'/'+file_name+".png", img)

	file_counter += 1


#
#
# Обрабатываем кадры в цикле
#
#
while True:
    # Получаем кадр
    status, image = frame.read()
    image_done = image.copy()

    faces = face.detectMultiScale(image, scaleFactor=1.8, minNeighbors=6, minSize=(110,110))

    for (x, y, w, h) in faces:
        cv2.rectangle(image_done, (x,y), (x+w,y+h), (0,255,64), 2)

    if isRecord and (len(faces) > 0):
        image_face_frame = image[y:y + h, x:x + w]
        image_face_frame = cv2.cvtColor(image_face_frame, cv2.COLOR_RGB2GRAY)
        save_frame(image_face_frame)
        image_done = add_record(image_done)

    cv2.imshow("Face", image_done)
    k = cv2.waitKey(30)

    # Обрабатываем нажатие клавиши ESC
    if k == 27:
        break

    # Обрабатываем нажатие клавиши r, которая включает или выключает запись видео
    if k == 114:
        if not isRecord:
            start_recording()  # Начинаем запись
            isRecord = True
        else:
            stop_recording()  # Закончим запись
            isRecord = False

frame.release()
cv2.destroyAllWindows()
