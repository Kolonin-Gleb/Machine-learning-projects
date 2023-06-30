import sys
import os
import numpy as np
import cv2
import math
from PIL import Image, ImageEnhance

os.system('cls')

# Получаем кадр с видеокамеры
frame = cv2.VideoCapture(0)

# Создаем объект для обнаружения лица
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Статусы отображения
isBlurred = False

# Обрабатываем кадры в цикле
while True:
    # Получаем кадр
    status, image = frame.read()
    result_image = image.copy()
    image_face = 0

    faces = face.detectMultiScale(image, scaleFactor=2, minNeighbors=6, minSize=(110,110))
    # scaleFactor - параметр, определяющий "тщательность" поиска лица на изображении. Чем он ближе к 1,
    # тем больше времени уйдет на поиск лица, тем дольше будет происходить этот поиск. При больших
    # значениях есть риск пропустить лица

    # Наложение прямоугольника на распознанное лицо
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 64), 2)
        
        image_face = image[y:y+h, x:x+w] # Сохранение только лица
        # cv2.imshow("cropped face", image_face) # Для теста
        image_face = Image.fromarray(image_face)
        
    # image_face - <class 'numpy.ndarray'>

        if isBlurred:
            # Применение размытия
            image = cv2.GaussianBlur(image, (49, 49), 0)
            image = Image.fromarray(image)
            # Наложение неразмытого лица
            if image_face != 0:
                image.paste(image_face, [x, y])
            image = np.asarray(image, dtype='uint8') # для cv2


    cv2.imshow("Face recognition blurred backgound", image)
    esc = cv2.waitKey(30)

    if cv2.waitKey(30) == 121 or cv2.waitKey(30) == 81:
        isBlurred = not isBlurred
    if esc == 27:
        break

frame.release()
cv2.destroyAllWindows()

# Необходимо использовать функцию обнаружения лица.
#   При нажатии на клавишу [y] сделать так, чтобы лицо осталось четким, а фон был размыт
#    Для размытия можно использовать функцию GaussianBlur
#    Функция GaussianBlur (размытие по Гауссу) принимает 3 параметра:
#    1. Исходное изображение.
#    2. Кортеж из 2 положительных нечётных чисел. Чем больше числа, тем больше сила сглаживания.
#    3. sigmaX и sigmaY. Если эти параметры оставить равными 0, то их значение будет рассчитано автоматически
