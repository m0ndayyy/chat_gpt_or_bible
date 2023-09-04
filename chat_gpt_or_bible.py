import openai
import pythonbible
import random


openai.api_key = ""
messages = [{"role":"system", "content":"You will respond with the same style that the bible is written in."}]
messages.append({"role":"user", "content":"please generate a fake bible verse as if could be found somewhere in the bible."})
chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
reply = chat.choices[0].message.content
print(reply)


book = random.randint(1, 66)
max_chapters = pythonbible.get_number_of_chapters(pythonbible.Book(book))
chapter = random.randint(1, max_chapters)
max_verses = pythonbible.get_number_of_verses(pythonbible.Book(book), chapter)
verse = random.randint(1, max_verses)
quote_id = pythonbible.get_verse_id(pythonbible.Book(book), chapter, verse)
quote = pythonbible.get_verse_text(quote_id)
print(quote)