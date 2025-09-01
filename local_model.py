from openai import OpenAI
import json


class LocalModel:
    def __init__(self, base_url):
        self.base_url = base_url + "/v1"
        self.daily_prompt = "Ты являешься саммарайзером заметок в ежедневнике. Тебе необходимо анализировать заметки. Твоим ответом должен быть текст только с кратким содержанием заметки."
        self.monthly_prompt = "Ты являешься саммарайзером заметок в ежедневнике. Тебе необходимо анализировать краткое содержание заметок за месяц. Твоим ответом должен быть текст только с кратким содержанием и анализом того, что происходило за месяц."


    def set_model(self):
        self.client = OpenAI(base_url=self.base_url, api_key="lm-studio")

    def analyse_daily_note(self, note):
        print(note)
        note = json.dumps(note, ensure_ascii=False)
        completion = self.client.chat.completions.create(
                 model="model-identifier",
                 messages=[
                   {"role": "system", "content": self.daily_prompt},
                   {"role": "user", "content": note}
                 ],
                 temperature=0.7,
               )
        result = completion.choices[0].message.content
        return result

    def analyse_monthly_notes(self, notes):
        notes = json.dumps(notes, ensure_ascii=False)
        completion = self.client.chat.completions.create(
                 model="model-identifier",
                 messages=[
                   {"role": "system", "content": self.monthly_prompt},
                   {"role": "user", "content": notes}
                 ],
                 temperature=0.7,
               )
        result = completion.choices[0].message.content
        return result
