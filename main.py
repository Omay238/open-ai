import os
import openai
from colorama import Fore, init

init()
openai.api_key = os.environ['OPENAI_API_KEY']
start_sequence = f"{Fore.RED}\nAI: "
restart_sequence = f"{Fore.GREEN}\nHuman: "
text = f"{Fore.WHITE}The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.{Fore.GREEN}\n\nHuman: Hello, who are you?{Fore.RED}\nAI: I am an AI created by OpenAI. How can I help you today?{Fore.GREEN}\nHuman: "
while True:
	os.system('clear')
	text = text + input(text) + start_sequence
	response = openai.Completion.create(engine="text-davinci-001", prompt=text, temperature=0.9, max_tokens=150, top_p=1, frequency_penalty=0.6, presence_penalty=0, stop=[" Human:", " AI:"])
	text = text + response.choices[0].text.replace("\n", "") + restart_sequence