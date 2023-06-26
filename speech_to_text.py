import speech_recognition as sr
import tempfile

def speech_to_text(audio) -> str:

    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)
    return text
