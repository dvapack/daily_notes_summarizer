from user_interface import UserInterface
from dataloader import Dataloader

ui = UserInterface()
ui.greeting_message()
link = ui.get_link()
dataloader = Dataloader()
md_files = dataloader.read_all_md_files(link)
