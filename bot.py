from aiogram import *
import openai
 
GPTAPIKEY = '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'
TGBOTTOKEN = '6105952763:AAF0kAeNO2eqZ4NUc-SFRiM8kB7KkH3T50Q'
 
bot = Bot(token =TGBOTTOKEN)
dp = Dispatcher(bot)
openai.api_key = GPTAPIKEY

@dp.message_handler(commands='start')
async def hello(message:types.message):
    await message.answer(f'Привет {message.from_user.username}, я бот GPT! Давай поболтаем ^.^')
    await message.answer('Напиши мне что-нибудь')
 
@dp.message_handler(content_types='text')
async def get_text_messages(message:types.message):
    completion = openai.Completion.create(engine="text-davinci-003", 
                                          prompt=message.text, 
                                          temperature=0.5, 
                                          max_tokens=1000)
    await bot.send_message(message.from_user.id, completion.choices[0]["text"])  


if __name__ == '__main__':
    executor.start_polling(dp)
