import cv2
import numpy as np

# Получаю видео
frame = cv2.VideoCapture(0)

print(type(frame))

# Стутусы отображения
isFlip = False
isAddRed = False

# Обрабатка кадров в цикле
while True:
    status, hsv_img = frame.read() # Запись изображений с камеры.
    hsv_img = hsv_img.copy() # Превращение изображения в массив np
    # print(type(hsv_img))

    # flip(изображение, код поворота)
    # -1 - both direction  - обеспечит поворот на 180 градусов
    # 0 - horizontal flip - переворот
    # 1 - vertical flip   - зеркалирование

    if isFlip:
        hsv_img = cv2.flip(hsv_img, -1)

    # Меняем цветовую модель с HSV на BGR
    # cvtColor() - меняет цветовую модель изображения
    if isAddRed:
        rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
        # rgb_img[(..., 0)] - только значения хранящиеся по 0 индексу массива.
        rgb_img[(..., 0)] = rgb_img[(..., 0)] * 1.10 # 1.10 = добавить 10 %
        np.clip(rgb_img, 0, 255) # Возращаем значения цвета в приемлемый диапозон.
        hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)

    hsv_img_edited = hsv_img.copy()

    cv2.imshow("TV", hsv_img_edited)
    k = cv2.waitKey(30) # Количество кадров в секунду + время ожидания нажатия

    # print(k)    
    # 84 - T 116 - t 
    # 83 - S 115 - s 
    # 27 - Esc

    if k == 83 or k == 115: # 83 - S 115 - s 
        isAddRed = not isAddRed
    if k == 116 or k == 84: # 84 - T 116 - t 
        isFlip = not isFlip
    if k == 27: # 27 - Esc
        break

frame.release()
cv2.destroyAllWindows()
