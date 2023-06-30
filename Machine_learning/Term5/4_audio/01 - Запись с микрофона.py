import pyaudio
import wave

# Параметры записи звука:

CHUNK = 1024  # определяет форму ауди сигнала
FRT = pyaudio.paInt16  # шестнадцатибитный формат задает значение амплитуды
CHAN = 1  # количество каналов записи звука
RT = 44100  # частота
REC_SEC = 5  # длина записи
OUTPUT = "audio1.wav"  # Выходной файл

# Создаем объект, способный записать аудио
p = pyaudio.PyAudio()

# Отскроем поток для записи, передав нужные параметры
stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True, frames_per_buffer=CHUNK)

print("rec")
frames = []  # записываем значения значения дискретизации
for i in range(0, int(RT / CHUNK * REC_SEC)):
    data = stream.read(CHUNK)  # Читаем данные об оцифрованной амплитуде из потока
    frames.append(data)  # добавляем данные в массив
print("done")

stream.stop_stream()  # останавливаем и закрываем поток
stream.close()
p.terminate()

# Записываем данные в файл
w = wave.open(OUTPUT, 'wb')
w.setnchannels(CHAN)
w.setsampwidth(p.get_sample_size(FRT))
w.setframerate(RT)
w.writeframes(b''.join(frames))
w.close()
