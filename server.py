import unicron_pb2_grpc
from text_similarity import get_similarity
import unicron_pb2 as unicron
import grpc
from concurrent import futures
from speech_to_text import speech_to_text
# from text_to_speech import text_to_audio
import os

class UnicronService(unicron_pb2_grpc.UnicronServicer):
    """Missing associated documentation comment in .proto file."""

    # def audiolize(self, request, context):
    #     audio = text_to_audio(request.text)
    #     return unicron.AudiolizeResponse(audio=audio)

    def textify(self, request, context):
        text = speech_to_text(request.audio)
        return unicron.TextifyResponse(text=text)

    def similarity(self, request, context):
        res = get_similarity(request.text, request.answers)
        print(res)
        return unicron.SimilarityResponse(similarity=res)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    unicron_pb2_grpc.add_UnicronServicer_to_server(UnicronService(), server)
    
    url = f'{os.environ["UNICRON_HOST"]}:{os.environ["UNICRON_PORT"]}'
    server.add_insecure_port(url)
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print('Hi guys')