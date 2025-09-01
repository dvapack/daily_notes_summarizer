from user_interface import UserInterface
from dataloader import Dataloader
from local_model import LocalModel

ui = UserInterface()
ui.image()
ui.greeting_message()
link = ui.get_link()
dataloader = Dataloader()
md_files = dataloader.read_all_md_files(link)
base_url = ui.get_base_url()
model = LocalModel(base_url)
model.set_model()
daily_notes = []
for md_file in md_files.values():
    daily_notes.append(model.analyse_daily_note(md_file['content']))
print(daily_notes)
