import os
import shutil
from flask import Flask, render_template, request, jsonify, flash, url_for
import requests
# from flask_socketio import SocketIO
from PIL import Image
from img_gemini import gemini_img
from text_gemini import gemini_text
from fasttext import load_model
from gtts import gTTS
from text_standardized import remove_special_chars, encode_string
import speech_recognition as sr
import pyttsx3
# import time
# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))

# import time

# start_time = time.clock()
# main()
# print(time.clock() - start_time, "seconds")

app = Flask(__name__)
app.config['SECRET_KEY'] = "caas-srk"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_message', methods=['POST'])
def process_message():

    user_input = request.form.get('user-input')
    image_file = request.files.get('image-input')


    model = load_model('models/model_response_classification.bin')
    predicted_label = model.predict(user_input)
    prediction = predicted_label[0][0]

    if prediction == '__label__Rasa':
        r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_input})
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")
        bot_response = f"CTU Bot: {bot_message}"
        # text_to_speech(bot_response)
        print(prediction)
        print(bot_response)
    else:
        if image_file:
            image_path = f"uploads/{image_file.filename}"
            image_file.save(image_path)
            bot_response = f"CTU Bot: {gemini_img(image_path, user_input)}"
        else:
            bot_response = f"CTU Bot: {gemini_text(user_input)}"
        # text_to_speech(bot_response)
        print(prediction)
        print(bot_response)
        folder_path = "uploads"
        empty_directory(folder_path)
    return jsonify({'userInput': user_input, 'botResponse': bot_response})

def empty_directory(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
    except Exception as e:
        print(f"Lỗi: {e}")

@app.route('/voice-input', methods=['POST'])

def record():
    recognizer = sr.Recognizer()    
    with sr.Microphone() as source:
        print("Đang nghe...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='vi-VN')
        return render_template('index.html', text=text)
    except sr.UnknownValueError:
        error_message = "Không nhận diện được giọng nói."
        return render_template('index.html', error_message=error_message)
    except sr.RequestError as e:
        error_message = f"Lỗi kết nối đến API nhận diện giọng nói: {str(e)}"
        return render_template('index.html', error_message=error_message)

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
    app.run(debug=True, port=5002)