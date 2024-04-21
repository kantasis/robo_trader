#!/usr/local/bin/python3

# Imports
from os import environ
from openai import OpenAI

# Parameters
openai_key = environ['OPENAI_API_KEY']

# Main
client = OpenAI()

completion = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
      {
         "role": "system", 
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
      },
      {
         "role": "user", 
         "content": "Compose a poem that explains the concept of recursion in programming."
      }
   ]
)

print(completion.choices[0].message)

