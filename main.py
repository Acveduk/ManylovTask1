from moviepy.editor import *
from moviepy.config import change_settings
from setting import *

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


def ticker(text, color, font, img):
    screensize = (100, 100)  # Устанавливаем размер изображения
    img = ImageClip(img).set_duration(3)  # Создаем видео из изображения
    txt = TextClip(txt=text, color=color, font=font, fontsize=70).set_duration(
        3)  # Создаем видео с текстом и настраиваем его
    size = txt.size[0] if txt.size[0] >= 100 else 100

    video = CompositeVideoClip([img, txt.set_pos(lambda t: (0 - t * ((size-99)/3), 'center'))],
                               size=screensize)  # Объединяем 2 видео в одно

    # lambda t: (100 - t, 'center')
    video.write_videofile(f'video.mp4', fps=60, codec='mpeg4')  # записываем видео в файл


print("БЕГУЩАЯ СТРОКА\n\n"
      "Введите текст: ")
text = str(input())
color = color()
font = font()

ticker(text, color, font, "background.jpg")
