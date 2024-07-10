#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tempfile
import speech_recognition as sr
from gtts import gTTS
import pygame
import os

# تهيئة التعرف على الصوت
recognizer = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("تحدث الآن...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ar-SA")
            print("لقد قلت: " + text)
            return text
        except sr.UnknownValueError:
            print("لم يتم التعرف على الصوت")
            return None
        except sr.RequestError:
            print("خطأ في الخدمة")
            return None

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"خطأ في الحساب: {e}")
        return None

def text_to_speech(text):
    tts = gTTS(text=text, lang='ar')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_filename = fp.name
        tts.save(temp_filename)
    
    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Add a small delay to avoid high CPU usage
    
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    os.remove(temp_filename)

if __name__ == "__main__":
    exit_keyword = "انتهيت"
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        attempts += 1

        # الحصول على المدخلات الصوتية
        expression = get_audio()
        if expression:
            # Check for exit keyword
            if exit_keyword in expression:
                print("يتم الآن إنهاء البرنامج.")
                text_to_speech("يتم الآن إنهاء البرنامج.")
                break

            # حساب الناتج
            result = calculate(expression)
            if result is not None:
                print(f"الناتج هو: {result}")
                # تحويل الناتج إلى صوت
                text_to_speech(f"الناتج هو: {result}")


# In[ ]:




