import google.generativeai as genai

genai.configure(api_key="AIzaSyBkrqxHG2q0vyF1TdFLrpdJOnBEiZbAxxk")

# Set up the model
generation_config_img = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings_img = [
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

model_img = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config_img,
                              safety_settings=safety_settings_img)

def gemini_text(prompt):
  response = model_img.generate_content(prompt)
  text = (response.text)
  return text

