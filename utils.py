import bcrypt
import openai
#from openai import AsyncOpenAI
from config import settings

openai.api_key = settings.open_api_key
#client = AsyncOpenAI(api_key=settings.open_api_key)

def hash_password(password: str) -> str:
    bytePwd = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(bytePwd, mySalt)
    pwd_hash = pwd_hash.decode('utf-8')

    return pwd_hash

def verify_password(unhashed_password: str, hashed_password: str):
    bytePwd1 = unhashed_password.encode('utf-8')
    bytePwd2 = hashed_password.encode('utf-8')
    return bcrypt.checkpw(bytePwd1, bytePwd2)

def generate_tags(input):
    messages = [
        {"role": "user",
         "content": """Generate three single words based on the content and feeling of the inputted text, these will be the tags that are assigned to the text. Your output should 
         only be a list of string, in this form: ["Tech", "News", "Funny"]. Make sure the first letter of each tag is capitalized' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply
    '''messages.append({"role": "user", "content": f"{input}"})
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    return response'''