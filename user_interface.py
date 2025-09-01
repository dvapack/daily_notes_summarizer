from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

class UserInterface:
    def __init__(self):
        self.separator = "-----------------------------------------------------------"
        self.image_url = "console_pic.jpg"

    def image(self):
        width=50
        enhance_contrast=True
        use_extended_charset=True
        dithering=True

        img = Image.open(self.image_url)
        img = img.convert('L')

        if enhance_contrast:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(2.0)
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.5)

        aspect_ratio = img.height / img.width
        height = int(width * aspect_ratio * 0.55)

        if dithering:
            img = img.resize((width * 2, height * 2), Image.LANCZOS)
            img = img.resize((width, height), Image.LANCZOS)
        else:
            img = img.resize((width, height), Image.LANCZOS)

        pixels = np.array(img)

        if use_extended_charset:
            chars = ["@", "#", "W", "B", "8", "&", "M", "*", "o", "a", "h", "k",
                    "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C",
                    "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j",
                    "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]",
                    "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";",
                    ":", ",", "\"", "^", "`", "'", ".", " "]
        else:
            chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

        pixels = pixels.astype(np.float32)
        pixels = (pixels - pixels.min()) / (pixels.max() - pixels.min()) * 255
        pixels = pixels.astype(np.uint8)

        ascii_art = ""
        for row in pixels:
            for pixel in row:
                brightness = 255 - pixel
                index = int(brightness / 255 * (len(chars) - 1))
                ascii_art += chars[index]
            ascii_art += "\n"

        print(ascii_art)
        return

    def greeting_message(self):
        print(self.separator)
        print("Добро пожаловать в саммарайзер заметок.")
        print("Для начала работы настоятельно рекомендуется прочитать гайд по ссылке:")
        print("https://github.com/dvapack/daily_notes_summarizer/readme.md")
        print(self.separator)
        return

    def get_link(self):
        print("Предоставьте ссылку на папку с заметками для анализа:")
        link = str(input())
        return link

    def get_model(self):
        print(self.separator)
        print("Выберите модель для использования:")
        print("1 - для локальной модели")
        print("2 - для Google Gemini")
        model = int(input())
        return model

    def get_base_url(self):
        print(self.separator)
        print("Гайд по использованию локальной модели находится по ссылке: ")
        print("https://github.com/dvapack/daily_notes_summarizer/readme.md")
        print("Для использования локальной модели необходимо ввести base_url: ")
