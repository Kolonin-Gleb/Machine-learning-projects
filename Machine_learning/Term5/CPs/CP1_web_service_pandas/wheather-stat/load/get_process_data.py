import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# Папка, куда будут сохраняться полученные и обработанные данные для отчёта
out_dir = "../app/static/"

# Загрузка всех таблиц со страницы

df_t = pd.read_html('http://weatherarchive.ru/Temperature/Moscow/September-2022', encoding='utf-8')
len(df_t) # Число таблиц на сайте

df_wheater = df_t[2] # Нужная мне таблица в виде df

# Таблица в ее исходном виде – параметры погоды за месяц
df_wheater.columns = ["День месяца", "Среднесуточная температура", "Средняя влажность", "Атмосферное давление", "Скорость ветра"]
df_wheater

# Запись таблицы в файл формата HTML

# Указать путь до места, где необходимо сохранить таблицу # ../app/static/
df_wheater.to_html(out_dir+'table.html', index=False)

# -- Сделаю график изменения температуры. Сохраню его в .png

dates = list(df_wheater['День месяца'])
dates = [d.split(' ')[0] for d in dates]

temperature = list(df_wheater['Среднесуточная температура'])
temperature = [float(t[1:-2]) for t in temperature]

fig = plt.figure(figsize=(11, 6))
ax = fig.add_subplot()

# Наносим надписи
ax.set_title("График изменения температуры в сентябре")

# Включаем отображение сетки
ax.grid(color = 'black',   #  цвет линий
        linewidth = 1,       #  толщина
        linestyle = ':')     #  начертание

# Отрисовываем график линейной зависимости
ax.plot(dates, temperature, color='blue')
ax.legend()

# Сохранение в png
plt.savefig(out_dir+'temperature_change.png')

# -- Сделаю график изменения атм. давления. Сохраняю его в .png
pressure = list(df_wheater['Атмосферное давление'])

fig = plt.figure(figsize=(11, 6))
ax = fig.add_subplot()

# Наносим надписи
ax.set_title("График изменения Атмосферного давления в сентябре")

# Включаем отображение сетки
ax.grid(color = 'black',   #  цвет линий
        linewidth = 1,       #  толщина
        linestyle = ':')     #  начертание

# Отрисовываем график линейной зависимости
ax.plot(dates, pressure, color='blue')
ax.legend()

# Сохранение в png
plt.savefig(out_dir+'pressure_change.png')

# Сделаю столбч. диаграмму оранжевого цвета с показателями влажности. Сохраняю её в .png  -  

wet = list(df_wheater['Средняя влажность'])

plt.figure(figsize=(30, 14))


# Наносим надписи
plt.title("Изменения показателей влажности")
plt.rcParams['font.size'] = '30' # Размер шрифта

# Стандартная столбчатая диаграмма
plt.bar(dates, wet, color='orange')

# Сохранение в png
plt.savefig(out_dir+'wet_change.png')