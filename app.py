import os
import asyncio
import shutil
from flask import Flask, render_template, request, jsonify, flash, url_for
import requests
from PIL import Image
from img_gemini import gemini_img
from text_gemini import gemini_text
from fasttext import load_model
from gtts import gTTS
from text_standardized import remove_special_chars, encode_string
import speech_recognition as sr
import pyttsx3
import time
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig


app = Flask(__name__)
app.config['SECRET_KEY'] = "caas-srk"

load_classifier_start_time = time.time()
classifier = load_model('models/model_response_classification.bin')
load_classifier_elapsed_time = time.time() - load_classifier_start_time
print(f"Thời gian load model_response_classification: {load_classifier_elapsed_time} seconds")

load_rasa_start_time = time.time()
rasa_model_path = "api-rasa/models/20240101-155929-vibrato-gravel.tar.gz"
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook",type="http")
agent = Agent.load(rasa_model_path, action_endpoint=action_endpoint)
load_rasa_elapsed_time = time.time() - load_rasa_start_time
print(f"Thời gian load model_rasa: {load_rasa_elapsed_time} seconds")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_message', methods=['POST'])
async def process_message():
    start_time = time.time()
    user_input = request.form.get('user-input')
    image_file = request.files.get('image-input')
    print("-------------------------->",user_input)
    model_start_time = time.time()
    predicted_label = classifier.predict(user_input)
    prediction = predicted_label[0][0]
    model_elapsed_time = time.time() - model_start_time
    print(f"+Thời gian chạy model_response_classification: {model_elapsed_time} seconds")

    if prediction == '__label__Rasa':
        rasa_start_time = time.time()
        bot_message = await agent.handle_text(user_input)
        bot_response = f"CTU Bot: {bot_message}"
        print(bot_message)
        rasa_elapsed_time = time.time() - rasa_start_time
        print(f"+Thời gian chạy rasa: {rasa_elapsed_time} seconds")
    else:
        if image_file:
            image_path = f"uploads/{image_file.filename}"
            image_file.save(image_path)
            bot_response = f"CTU Bot: {gemini_img(image_path, user_input)}"
        else:
            user_input = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Hãy trả lời câu " + user_input + " một cách ngắn gọn"
            bot_response = f"CTU Bot: {gemini_text(user_input)}"
        # print(prediction)
        # print(bot_response)
        folder_path = "uploads"
        empty_directory(folder_path)

    elapsed_time = time.time() - start_time
    print(f"+Thời gian chạy process_message: {elapsed_time} seconds")

    return jsonify({'userInput': user_input, 'botResponse': bot_response})

def empty_directory(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
    except Exception as e:
        print(f"Lỗi: {e}")

@app.route('/record', methods=['POST'])
def record():
    asyncio.run(record_async())
    return "Recording..."

async def record_async():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Đang nghe...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='vi-VN')
        print(text)
    except sr.UnknownValueError:
        print("Không nhận diện được giọng nói.")
    except sr.RequestError as e:
        print(f"Lỗi kết nối đến API nhận diện giọng nói: {str(e)}")

@app.route('/speak', methods=['POST'])
def speak():
    text_to_speak = remove_special_chars(request.json['tts'])

    # Tạo đối tượng gTTS
    tts = gTTS(text=text_to_speak, lang='vi', slow=False)

    # Lưu file audio
    audio_path = f'static/audio/{encode_string(text_to_speak)}.mp3'
    tts.save(audio_path)

    # Trả về URL của file audio
    audio_url = request.host_url + audio_path
    return jsonify({'audio_url': audio_url})

if __name__ == '__main__':
    app.run(debug=True)
