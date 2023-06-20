import speech_recognition as sr

def speech_to_text(audio: str) -> str:
    audio_file = audio
    r = sr.Recognizer()
    return r.recognize_google(audio_file, language="ru-RU")
