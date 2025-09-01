from openai import OpenAI
import json


class LocalModel:
    def __init__(self, base_url):
        self.base_url = base_url
        self.daily_prompt = "Ты являешься саммарайзером заметок в ежедневнике. Тебе необходимо анализировать заметки. Твоим ответом должен быть текст только с кратким содержанием заметки."
        self.monthly_prompt = "Ты являешься саммарайзером заметок в ежедневнике. Тебе необходимо анализировать краткое содержание заметок за месяц. Твоим ответом должен быть текст только с кратким содержанием и анализом того, что происходило за месяц."
        
        
    def set_model(self):
        self.client = OpenAI(base_url=self.base_url, api_key="lm-studio")
    
    def analyse_daily_note(self, note):
        note
        