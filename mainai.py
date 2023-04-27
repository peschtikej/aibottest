import openai, os, dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv('OPEN_AI_KEY')

msg=[]

def get_response(message):
    msg.append({'role':'user', 'content':message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    answer=response['choices'][0]['message']['content']
    msg.append({'role':'assistant', 'content':answer})
    
    return answer

print('Приветствую тебя, уважаемый пользователь! Я - искусственный интеллект, созданный для того, чтобы помочь тебе в решении задач и достижении целей.\nВведите запрос: ')
while True:
   zap=input()
   print(get_response(zap))
   if zap=='Пока' or 'пока':
       break