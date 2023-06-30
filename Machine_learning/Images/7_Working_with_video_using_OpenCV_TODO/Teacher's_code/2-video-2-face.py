import sys
import numpy as np
import cv2
import math
from PIL import Image

# Получаем кадр с видеокамеры
frame = cv2.VideoCapture(1)

# Создаем объект для обнаружения лица
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

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
    # scaleFactor - параметр, определяющий "тщательность" поиска лица на изображении. Чем он ближе к 1,
    # тем больше времени уйдет на поиск лица, тем дольше будет происходить этот поиск. При больших
    # значениях есть риск пропустить лица

    for (x, y, w, h) in faces:
        cv2.rectangle(image_done, (x,y), (x+w,y+h), (0,255,64), 2)


    cv2.imshow("Face", image_done)
    k = cv2.waitKey(30)
    if k == 27:
        break

frame.release()
cv2.destroyAllWindows()
