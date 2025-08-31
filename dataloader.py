import os
import markdown

class Dataloader:
    def __init__(self):
        pass

    def read_all_md_files(self, folder_path):
        """
        Чтение всех .md файлов в указанной папке
        """
        md_files = {}

        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Папка {folder_path} не найдена. User дурак!")

        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"{folder_path} не является папкой. User дурак!")

        for filename in os.listdir(folder_path):
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        md_files[filename] = {
                            'content': content,
                            'html': markdown.markdown(content),
                            'path': file_path
                        }
                except Exception as e:
                    print(f"Ошибка при чтении файла {filename}: {e}")

        return md_files
