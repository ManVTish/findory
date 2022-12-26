# pafy for video/audio download
# import pafy

# FASTAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.project_variables import APP_HOST
from models.video import Video
from models.user_keyword import UserKeyword
from services.video_transcript import VideoTranscript

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[APP_HOST],
    allow_methods=['*'],
    allow_headers=['*']
)


# Request = {"user_video_id": "some_value"}
@app.post('/video')
def get_video_transcript(video_request: Video):
    video_id = video_request.user_video_id
    # video.user_video_id = video_id
    video_request.user_video_transcript = VideoTranscript.find_video_transcript(video_id)
    video_request.save()
    return video_request.pk


# Request = {"keyword": "some_value", "key_id": "some_pk"}
@app.post('/keyword')
def get_keyword_record(keyword_data: UserKeyword):
    video = Video.get(keyword_data.key_id)
    transcript = video.user_video_transcript
    return VideoTranscript.search_keyword(keyword_data.keyword, transcript)


@app.post('/video/keyword')
def find_keyword_timestamp(user_data: UserData):
    video_id = user_data.main_video_id
    keyword_data = user_data.keyword
    transcripts = VideoTranscript.find_video_transcript(video_id)
    return VideoTranscript.search_keyword(keyword_data, transcripts)

