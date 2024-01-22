# coding = <utf-8>

import PIL.Image


# img = 'D:\\CAAS\\api-rasa\\api-gemini\\img.png'
import google.generativeai as genai

genai.configure(api_key="AIzaSyBkrqxHG2q0vyF1TdFLrpdJOnBEiZbAxxk")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]
# import pathlib
# import textwrap
# from google.colab import userdata

# from IPython.display import display
# from IPython.display import Markdown
# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# img = PIL.Image.open('image.png')
# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content(img)

# print(response.text)
# response = model.generate_content(["Viết một bài đăng blog ngắn, hấp dẫn dựa trên bức ảnh này. Nó nên bao gồm mô tả về bữa ăn trong ảnh và nói về việc chuẩn bị bữa ăn trong hành trình của tôi.", img], stream=True)
# response.resolve()
# print(response.text)

# img = PIL.Image.open('score1.png')
# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content(img)

# print(response.text)
# response = model.generate_content(["Điểm của ngành Khoa học máy tính là bao nhiêu và mã ngành, ngành thi của nó một cách ngắn gọn", img], stream=True)
# response.resolve()
# print(response.text)

img = PIL.Image.open('bendmark.png')
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

# print(response.text)
response = model.generate_content(["Mã ngành Truyền thông đa phương tiện", img], stream=True)
response.resolve()
print(response.text)