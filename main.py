# pafy for video/audio download
# import pafy

# FASTAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.project_variables import APP_HOST
from models.user_data import UserData
from services.video_transcript import VideoTranscript

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[APP_HOST],
    allow_methods=['*'],
    allow_headers=['*']
)

# Request = {"main_video_id": "some_value", "keyword": "some_value"}
@app.post('/video/keyword')
def find_keyword_timestamp(user_data: UserData):
    video_id = user_data.main_video_id
    keyword_data = user_data.keyword
    transcripts = VideoTranscript.find_video_transcript(video_id)
    return VideoTranscript.search_keyword(keyword_data, transcripts)

