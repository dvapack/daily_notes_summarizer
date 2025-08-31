class UserInterface:
    def __init__(self):
        pass

    def greeting_message(self):
        print("Добро пожаловать в саммарайзер заметок.")
        print("Для начала работы настоятельно рекомендуется прочитать гайд по ссылке:")
        print("https://github.com/dvapack/daily_notes_summarizer/readme.md")
        return

    def get_link(self):
        print("Предоставьте ссылку на папку с заметками для анализа:")
        link = str(input())
        return link
