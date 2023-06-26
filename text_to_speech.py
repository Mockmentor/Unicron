from TTS.api import TTS


#tts_model = TTS_Model()
tts_model = TTS("tts_models/en/ljspeech/tacotron2-DDC")


def tts_to_file(text):
    path = tts_model.tts_to_file(text)
    file = open(path, "rb").read()
    return file
