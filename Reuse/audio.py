from pydantic import BaseModel
from fastapi import APIRouter, File, UploadFile, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydub import AudioSegment
import requests
import main
from io import BytesIO
import base64
from Reuse.Helper import Helper

router = APIRouter()
class Audio(BaseModel):
    userID: str
    token: str
    url: str
    begin: int
    end: int

@router.post("/api/deliver/audio/")
def post_audio(audioMeta: Audio):
    audio = requests.get(audioMeta.url, timeout=10)
    audioID = Helper.getAudioID(audio.url)
    original = AudioSegment.from_mp3(BytesIO(audio.content))
    begin = audioMeta.begin * 1000
    end = audioMeta.end * 1000
    section = original[begin:end]
    buf = BytesIO()
    section.export(buf, format="mp3")
    sendAudioToStorage(audioID, buf, audioMeta.userID, audioMeta.token)
    json_response = jsonable_encoder({"trimmed_audio_url": get_audio(audioMeta.userID, audioID)})
    return json_response

def sendAudioToStorage(audioID, sectionOfAudio, userID, token):
    main.storage.child(userID).child(audioID).put(sectionOfAudio, token)
    return "Delivered to storage"


@router.get("/api/receive/audio")
def get_audio(userID, audioID):
    print(main.storage.child(userID).get_url(audioID))
    return main.storage.child(userID).child(audioID).get_url("eyJhbGciOiJSUzI1NiIsImtpZCI6ImFiMGNiMTk5Zjg3MGYyOGUyOTg5YWI0ODFjYzJlNDdlMGUyY2MxOWQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZ2Vtcy10ZXN0LWI5MzRkIiwiYXVkIjoiZ2Vtcy10ZXN0LWI5MzRkIiwiYXV0aF90aW1lIjoxNjIzMzA1NDA2LCJ1c2VyX2lkIjoiZklJMHBLSzNQWU1DVFNOSG11czlXWkZtakRIMyIsInN1YiI6ImZJSTBwS0szUFlNQ1RTTkhtdXM5V1pGbWpESDMiLCJpYXQiOjE2MjMzMDU0MDYsImV4cCI6MTYyMzMwOTAwNiwiZW1haWwiOiJiZXJyeWJpbW9uQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImJlcnJ5Ymltb25AZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.D1XJRzMcUG9V4kdeFA9ZmB-9hRrTqxG9H66zUKBlxQFUJJTx4CE6CfWBjf03hmESrPLtK5OuPJHLWHdjt2w8i02tT4a5q1xU-cnittNyLiYTfCw71hu7mk4CHIjO-VzcIGWm98CewH4Lbt_8qQyj0I_0gGVtotLoDOvWMFIG9zP_OAHxtPMMDqVkTCVMuHU9n-mzy8GrT3q1cYaNoLCk2Td2FgQkHcBb2-AFbxWGg-7kE8Q3fXoBNQ23yJaSAdnkuFFnWz9ewGetGrjILupf6j98Ky3FlfKF-UUM7Q6szb9o52tPelJ3coVSncKb_HsAP_aL9mRSDWk6HuF3fdT5Sw")

# def getAudioID(audioUrl):
#     print(audioUrl)
#     audioUrlList = audioUrl.split("/")
#     return audioUrlList[3]
