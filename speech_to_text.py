import whisper
import tempfile


model = whisper.load_model("tiny")

def speech_to_text(audio) -> str:
    fd, path = tempfile.mkstemp()
    with open(fd, 'wb') as w:
        w.write(audio)
        result = model.transcribe(path, language='en')
    return result['text']
