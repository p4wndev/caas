import google.generativeai as genai
import time
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

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
# textex = "Điểm chuẩn ngành kĩ thuật phần mềm là bao nhiêu và nó có cao hơn Khoa học máy tính hông"
# prompt_parts = ["Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Cho biết điểm chuẩn ngành Kĩ thuật phần mềm là 26.3, khoa học máy tính 25.2 . Hãy trả lời câu " + textex +" một cách ngắn gọn"]
# response = model.generate_content(prompt_parts)
# print(response.text)
def gpt(prompt_parts):
  # textex = "Đại học cần Thơ thành lập vào ngày tháng năm nào"
  # prompt_parts = ["Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Hãy trả lời câu " + textex +" một cách ngắn gọn"]
  # gemini_start_time = time.time()
  # response = model.generate_content(prompt_parts)
  # text = response.text
  # gemini_elapsed_time = time.time() - gemini_start_time
  # print(f"Thời gian chạy rasa-text_gemini: {gemini_elapsed_time} seconds")
  # print(text)
  return "Test Gemini"

# chat = model.start_chat()
# response = chat.send_message('Xin chào, tui tên là Khanh và là sinh viên đại học Cần Thơ. Trả lời ngắn gọn vừa phải')
# print(response.text) 
# print("\n\n")
# response = chat.send_message("Tôi tên là gì. Trả lời ngắn gọn vừa phải")
# print(response.text) 
# print("\n\n")
# response = chat.send_message("Tôi học ở đâu. Trả lời ngắn gọn vừa phải")
# print(response.text)

# chat = model.start_chat()
# response = chat.send_message('Đại học cần Thơ thành lập vào ngày tháng năm nào. Trả lời ngắn gọn')
# print(response.text)
# print("\n\n")
# response = chat.send_message("Sai rồi 31 tháng 3 năm 1966 mới đúng. Trả lời ngắn gọn")
# print(response.text) 
# print("\n\n")
# response = chat.send_message("Địa chỉ cụ thể Đại học Cần Thơ. Trả lời ngắn gọn vừa phải")
# print(response.text) 
# print("\n\n")
# response = chat.send_message("Đường 3/2 mới đúng. Trả lời ngắn gọn vừa phải")
# print(response.text) 