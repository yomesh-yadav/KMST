from bardapi import Bard 

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY='AIzaSyDSlbzJkX0fbz9EpxHzLbtWnwLzZLPIvJQ'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

# print(response)

print(response.text)

# result = response.result

# # Extract the generated content from the result
# generated_content = result.candidates[0].content.parts[0].text

# # Print the generated content
# print(generated_content)

# Set the Bard API key
# bard.set_api_key('YOUR_API_KEY')

# # Send a request to the Bard API
# response = bard.send_request('What is the meaning of life?')

# # Get the Bard response
# bard_response = response.json()['response']

# # Print the Bard response
# print(bard_response)